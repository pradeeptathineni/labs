# Labs

`labs` is my working collection of problems I take apart, decisions I make, and things I build. The point is to practice critical thinking and show the work and reasoning when I have actually done it. An imported exercise is a plan, not an accomplishment.

The [catalog](CATALOG.md) shows the current work and the exercises waiting for me. The actual labs live under [`niches/`](niches/); [`.meta/`](.meta/README.md) holds the small tools that keep their metadata and index honest.

## Why the breadth?

Code is one way to practice problem-solving, but so are research, writing, design, and careful study. Take report generation: I could automate it for an operator, redesign it for its reader, measure its compute cost, or explain it well enough for the next maintainer. Those are related problems with different deliverables.

## How I organize a lab

```text
niches/<niche>/<domain>/<collection>/<lab>/
niches/<niche>/<domain>/<group>/<collection>/<lab>/
```

The niche describes the primary form of work (`code`, `study`, `writing`, and so on). The domain names the subject. The optional group gives me one useful navigation step, such as `aws` or `mit`. The collection groups a curriculum, course, certification, or project series. The lab is one work unit, which may contain several questions.

For example, [`roadmap.sh DevOps Projects`](niches/code/devops/roadmap-sh/) is an ordered collection of 26 starters. [`DevRoadmaps DevOps Projects`](niches/code/devops/devroadmaps/) is an unordered set of five project ideas. [`CLF-C02 practice`](niches/study/cloud/aws/clf-c02/) currently has a question bank and a bounded study-and-review problem set. All are unstarted.

The path gives each lab one physical home. `lab.json` records type, target skills, provenance, and status. Its `source.provider` points to the registry; a folder named `aws` or `mit` never implies a provider. The [maintenance guide](.meta/README.md) has the commands for creating, editing, syncing, and importing labs.

> [!IMPORTANT]
> I credit the people who created source material and keep required notices with copied content. Some sources are link-only, and linked third-party material can need its own review.
