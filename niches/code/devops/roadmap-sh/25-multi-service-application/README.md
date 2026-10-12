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
