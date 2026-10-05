#!/usr/bin/env python3
"""Adopt whole ThePlatformLab exercises and mocks from a pinned local checkout."""
import hashlib
import posixpath
import re
import sys
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import catalog
import workflow
import import_support
from markdown_it import MarkdownIt
from mdformat.renderer import MDRenderer

PROVIDER = 'platformlab-cka'
REPO = 'theplatformlab/CKA-Certified-Kubernetes-Administrator'


def pinned_target(value, path, revision, paths, image=False):
    parts = urlsplit(value)
    if parts.scheme or parts.netloc:
        return catalog.safe_url(value)
    relative = posixpath.normpath(posixpath.join(posixpath.dirname(path), unquote(parts.path))) if parts.path else path
    if relative == '..' or relative.startswith('../') or relative.startswith('/'):
        raise catalog.CatalogError(f'Upstream link escapes repository: {value}')
    if relative not in paths and not any(name.startswith(relative.rstrip('/') + '/') for name in paths):
        return None
    kind = 'blob' if relative in paths else 'tree'
    base = f'https://raw.githubusercontent.com/{REPO}/{revision}/' if image else f'https://github.com/{REPO}/{kind}/{revision}/'
    return base + quote(relative, safe='/') + ('?' + parts.query if parts.query else '') + ('#' + parts.fragment if parts.fragment else '')


def snapshot(text, path, revision, paths):
    parser = MarkdownIt('commonmark', renderer_cls=MDRenderer)
    environment = {}
    tokens = parser.parse(text, environment)
    headings = [(token.tag, tokens[index + 1].content) for index, token in enumerate(tokens) if token.type == 'heading_open']
    title = next((text for tag, text in headings if tag == 'h1'), None)
    if not title:
        raise catalog.CatalogError(f'Missing source title: {path}')
    task = next((text for tag, text in headings if tag == 'h2' and text.startswith('Tasks')), None)
    warnings = []
    def rewrite(items):
        for index, token in enumerate(items):
            if token.type in ('html_inline', 'html_block') and re.search(r'\b(?:href|src)\s*=', token.content, re.I):
                raise catalog.CatalogError('New raw HTML links need explicit adapter review')
            for attribute in ('href', 'src'):
                value = token.attrGet(attribute)
                if value:
                    resolved = pinned_target(value, path, revision, paths, image=attribute == 'src')
                    if resolved:
                        token.attrSet(attribute, resolved)
                    elif token.type == 'link_open':
                        # Missing source dependencies stay visible as text, never broken links.
                        warnings.append(f'Missing upstream target: {value}')
                        token.type, token.tag, token.nesting, token.content = 'text', '', 0, ''
                        closing = next(child for child in items[index + 1:] if child.type == 'link_close')
                        closing.type, closing.tag, closing.nesting = 'text', '', 0
                        closing.content = f' (upstream target unavailable: {value})'
                    else:
                        raise catalog.CatalogError(f'Missing upstream image needs review: {value}')
            if token.children:
                rewrite(token.children)
    rewrite(tokens)
    body = parser.renderer.render(tokens, parser.options, environment)
    url = f'https://github.com/{REPO}/blob/{revision}/{quote(path, safe="/")}'
    notice = f'# Upstream material — ThePlatformLab\n\nSource: [{path}]({url}) · revision `{revision}`\n\n> [!IMPORTANT]\n> This is upstream material, re-rendered only to pin its links. Hints, reference answers, verification examples and first-person anecdotes belong to the original author. They are not my Solution or my experience. See [the original MIT notice](LICENSE.txt).\n\n---\n\n'
    anchor = re.sub(r'[^\w\- ]', '', task.lower()).replace(' ', '-') if task else None
    return title, url + ('#' + anchor if anchor else ''), notice + body, warnings


def inventory(checkout, sources):
    catalog.require_copy_permission(PROVIDER, sources)
    revision, initial = workflow.git_checkout(checkout, REPO, ['LICENSE', 'README.md'])
    license_text = initial['LICENSE'].decode()
    if 'MIT License' not in license_text or 'Permission is hereby granted' not in license_text:
        raise catalog.CatalogError('The committed license needs a new review')
    paths = import_support.committed_paths(checkout, revision)
    selected = [path for path in paths if re.fullmatch(r'exercises/[0-9]+-[a-z0-9-]+/README\.md', path) or re.fullmatch(r'mock-exams/MOCK-EXAM-[0-9]+\.md', path)]
    if not selected:
        raise catalog.CatalogError('No complete exercise or mock files found')
    _, content = workflow.git_checkout(checkout, REPO, selected)
    items = []
    stems = [Path(path).parent.name.split('-', 1)[1] for path in selected if path.startswith('exercises/')]
    for path in sorted(selected):
        exercise = path.startswith('exercises/')
        title, url, copied, warnings = snapshot(content[path].decode(), path, revision, paths)
        if exercise:
            number, stem = Path(path).parent.name.split('-', 1)
            slug = stem + ('-' + number if stems.count(stem) > 1 else '')
        else:
            slug = Path(path).stem.lower()
        definition = f'Work through the complete [upstream {"task set" if exercise else "mock assessment"}]({url}) at this pinned revision. Keep the attempt, verification evidence and reasoning together as one {"exercise" if exercise else "problem set"}.'
        caution = '\n\nSource inconsistency to review before execution: Pod Basics requests `nginx:1.27`, while one supplied command uses `nginx:1.28`. No cluster validation has been performed.' if path == 'exercises/01-pod-basics/README.md' else ''
        if warnings:
            caution += '\n\nSource link limits: ' + '; '.join(warnings) + '. The snapshot labels these as unavailable.'
        readme = f'# {title}\n\nSource: [ThePlatformLab]({url})\n\n## Exercise Definition\n\n{definition}\n\nThe [upstream snapshot](source/UPSTREAM.md) includes the author’s hints, anecdotes and reference material, separately from my work. Its execution prerequisites and exam-alignment claims need review before an attempt.{caution}\n\n## Solution\n'
        descriptor = {'title': 'ThePlatformLab exercises' if exercise else 'ThePlatformLab mock exams', 'has_subdomain': True, 'ordered': True, 'tools': ['kubernetes'], 'goals': ['cka']}
        files = {'README.md': readme, 'source/UPSTREAM.md': copied, 'source/LICENSE.txt': license_text,
                 'source/item.json': catalog.json_text({'path': path, 'revision': revision, 'sha256': hashlib.sha256(content[path]).hexdigest(), 'handling': 'attributed upstream snapshot with pinned links', 'warnings': warnings})}
        items.append({'id': path, 'track': 'exercises' if exercise else 'mocks', 'data': {'title': title, 'slug': slug, 'type': 'exercise' if exercise else 'problem-set', 'skills': ['orchestration', 'troubleshooting'], 'source_url': url, 'revision': revision, 'collection_descriptor': descriptor}, 'files': files})
    return items


def main():
    parser = import_support.parser(__doc__)
    args = parser.parse_args()
    try:
        sources = catalog.load_sources()
        import_support.adopt(args, inventory(args.checkout, sources), PROVIDER, sources)
    except (catalog.CatalogError, OSError, ValueError, EOFError, KeyboardInterrupt) as error:
        if isinstance(error, (EOFError, KeyboardInterrupt)):
            print('\nNo changes made.')
            return 0
        print(f'error: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
