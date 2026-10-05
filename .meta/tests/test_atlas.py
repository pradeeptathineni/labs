"""Plans use the same subject rules as adopted work, without creating work."""
import json

from test_labs import RepositoryCase


class AtlasTests(RepositoryCase):
    def plan(self, *opportunities):
        (self.root / "README.md").write_text("# Fixture\n")
        value = {"goals": {}, "niche_guidance": [], "opportunities": list(opportunities), "unresolved_sources": []}
        (self.root / ".meta/catalog/atlas.json").write_text(json.dumps(value))

    def opportunity(self, identity, path, subdomain=False, provider="created"):
        return {"id": identity, "title": identity, "provider": provider,
                "materials_url": "https://example.com/material", "target": {"collection_path": path, "has_subdomain": subdomain, "tools": ["python"], "goals": ["personal-goal"]},
                "unit": "One bounded task", "lab_type": "exercise", "priority": "later", "adoption": "adaptation",
                "deliverable": "A reasoned result", "evidence_scope": "Index inspected", "checked_on": "2026-10-04"}

    def test_plans_matching_and_generation_are_separate_from_lifecycle(self):
        lab = self.init("code", "systems", "tasks", "Existing", "--source", "roadmap-sh", "--source-url", "https://example.com/task")
        path = lab.parent.relative_to(self.root).as_posix()
        one = self.opportunity("one", path, provider="roadmap-sh")
        other = self.opportunity("other", path, provider="exercism")
        future = self.opportunity("future", "niches/research/systems/distributed/mit/course", True, "roadmap-sh")
        self.plan(one, other, future)
        before = (lab / "lab.json").read_bytes()
        result = self.command("scripts", "catalog.py")
        self.assertEqual(result.returncode, 0, result.stderr)
        listed = self.command("scripts", "atlas.py", "--list")
        self.assertIn("one | later | 1 adopted", listed.stdout)
        self.assertIn("other | later | 0 adopted", listed.stdout)
        self.assertFalse((self.root / "niches/research").exists())
        atlas = (self.root / "PRACTICE-ATLAS.md").read_bytes()
        self.assertNotIn(b'](niches/research', atlas)
        self.assertEqual(self.command("scripts", "catalog.py").returncode, 0)
        self.assertEqual(atlas, (self.root / "PRACTICE-ATLAS.md").read_bytes())
        self.assertEqual(before, (lab / "lab.json").read_bytes())
        self.assertEqual(self.command("scripts", "atlas.py", "--check").returncode, 0)
        (self.root / "PRACTICE-ATLAS.md").write_text("stale")
        self.assertNotEqual(self.command("scripts", "atlas.py", "--check").returncode, 0)
        self.assertEqual((self.root / "PRACTICE-ATLAS.md").read_text(), "stale")

    def test_proposed_boundaries_collisions_and_traversal_fail_before_writes(self):
        for bad, expected in [
            (self.opportunity("bad", "niches/study/cloud/aws/tasks", False), "Subject boundary"),
            (self.opportunity("bad", "niches/code/cloud/aws/tasks/nested", True), "both collection and container"),
            (self.opportunity("bad", "niches/code/cloud/../elsewhere"), "Invalid proposed"),
        ]:
            self.plan(self.opportunity("one", "niches/code/cloud/aws/tasks", True), bad)
            result = self.command("scripts", "atlas.py", "--list")
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected, result.stderr)
            self.assertEqual(list((self.root / "niches").iterdir()), [])
