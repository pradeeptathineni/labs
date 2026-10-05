# Labs

`labs` is my working collection of problems I take apart, decisions I make, and things I build. The point is to practice critical thinking and show the work and reasoning when I have actually done it. An imported exercise is a plan, not an accomplishment.

The [visual workbench](https://pradeeptathineni.github.io/labs/) and [catalog](CATALOG.md) show the current work and the exercises waiting for me. The [practice atlas](PRACTICE-ATLAS.md) maps researched options I might adopt next. The actual labs live under [`niches/`](niches/); [`.meta/`](.meta/README.md) holds the small tools that keep their metadata and index honest.

## Why the breadth?

Code is one way to practice problem-solving, but so are research, writing, design, and careful study. Take report generation: I could automate it for an operator, redesign it for its reader, measure its compute cost, or explain it well enough for the next maintainer. Those are related problems with different deliverables.

## How I organize a lab

```text
niches/<niche>/<domain>/[<subdomain>/][<group>/...]<collection>/<lab>/
```

The niche describes the primary form of work (`code`, `study`, `writing`, and so on). The domain and optional subdomain name the subject: `devops`, `cloud/aws`, or `systems/distributed`. After the subject, any groupings organize providers, programs, or collections. A collection holds the lab units; one lab may contain several questions.

For example, `study/systems/mit/course-abc` is a course under Systems, while `study/systems/distributed/mit/course-abc` is under Distributed Systems. MIT organizes the course; it is not part of the subject. A collection can also combine providers, as `study/cloud/aws/clf-c02` does. The catalog brings collections with the same domain and subdomain together across niches.

The path gives each lab one physical home. A collection descriptor marks whether the optional subdomain is present; names still come from the path. `lab.json` records type, target skills, provenance, and status. Its `source.provider` points to the registry; a folder named `aws` or `mit` never implies a provider. The [maintenance guide](.meta/README.md) has the commands for creating, editing, syncing, and importing labs.

> [!IMPORTANT]
> I credit the people who created source material and keep required notices with copied content. Some sources are link-only, and linked third-party material can need its own review.

Kubernetes practice and conceptual reviews share `devops/orchestration`, with `kubernetes` as a browsing group and tool. Python language practice belongs in `programming/python`; ML implemented in Python belongs in `ai/machine-learning`. AWS certification work uses `cloud/aws` with short collection names such as `dop-c02`. Goals connect related work across those homes.
