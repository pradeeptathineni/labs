# Multi-Service Application

Source: [roadmap.sh](https://roadmap.sh/projects/multiservice-docker)

## Exercise Definition

Read the [original exercise definition](https://roadmap.sh/projects/multiservice-docker).

## Solution

### Starting choices, 2026-10-12

- Randomly drew this lab and Service Discovery from Blue-Green Deployment, Multi-Service Application, and Service Discovery. Their required work can run locally.
- Dockerized Service and Multi-Container Application also need remote deployment. Leave those planned while no cloud server is available.
- Use Docker Desktop and Compose for a small notes app: React, Express, MongoDB, Redis, and nginx. Only nginx opens a host port, on loopback.
- Use separate custom Node base images for the API and web build. Keep package locks and image digests. Serve the built web files from a small nginx image.
- Use named volumes, file-mounted database secrets, health checks, and rotated container logs. Compose already owns those jobs.
- Finish after checking the web page, writes, cache use, persistence, bad input, dependency failures, recovery, and cleanup. No AWS deployment or production claim is part of this attempt.

### First build findings

- The host npm command used Node 16 even though a newer Node was installed. Use the pinned Node 24 container for builds.
- The first package audit found advisories for Vite 7.1.7. This draft needs a patched build package before completion.
- The five-service files are a draft. Live checks and the package correction still remain.
- Changed Vite to 7.3.7 after reading the audit's affected versions. The updated package lock audit reported zero advisories. Live stack checks still remain.
