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
- MongoDB 8.0 refused Docker Desktop's Linux 7.0.12 kernel. Its [reported issue](https://jira.mongodb.org/browse/SERVER-121912) and [release notes](https://www.mongodb.com/docs/manual/release-notes/8.2/) cover this kernel range. Use pinned MongoDB 7.0 for this local attempt instead of changing the host kernel or bypassing the startup check.

### Run

```bash
cd niches/code/devops/roadmap-sh/25-multi-service-application

# Create a local password once. Keep it when reusing the database volume.
mkdir -p .secrets
(umask 077; test -f .secrets/mongo-password || openssl rand -hex 24 > .secrets/mongo-password)

# Build the two custom bases, then run the five services
docker build -f api/base.Dockerfile -t labs-notes-api-base:local api
docker build -f web/base.Dockerfile -t labs-notes-web-base:local web
docker compose up --build --wait --wait-timeout 120

# Open http://127.0.0.1:18250 and check the API and store recovery
python3 check.py
docker compose ps
docker compose logs --tail 20

# Stop the app but keep saved notes
docker compose down

# Remove this lab's saved notes only when they are no longer needed
docker compose down --volumes
```

- `check.py` creates a test note, recreates the containers, and briefly stops each store. Run it only against this local lab.
- [Compose secrets](https://docs.docker.com/compose/how-tos/use-secrets/) mount the password file into MongoDB and the API. The ignored host file is plain text, not an encrypted vault.
- This is an unauthenticated local notes app. MongoDB uses a lab admin account. Before any shared deployment, add app authentication, a database account with only the needed permissions, TLS, and a backup plan.
- Redis caches reads for ten seconds. A database outage can still leave a cached read available. Concurrent writes and cache updates are not one transaction, and a write followed by a cache failure can return an error after the database saved it.

### Checks, 2026-10-12

- Docker Desktop 4.92.0, Engine 29.8.0, Compose 5.5.1, and Linux 7.0.12 ran the stack. All five services became healthy.
- The containers reported Node 24.21.0, MongoDB 7.0.43, Redis 7.4.11, and nginx 1.28.3. Upstream images are pinned by digest. npm packages are locked. The two custom bases use local tags and must be rebuilt when package locks change.
- `python3 check.py` passed: served page, empty and long titles, malformed JSON, note creation, cache miss then hit, saved data after container recreation, and HTTP 503 during each store outage followed by recovery.
- Opened the React page in the browser, saved `Saved through the browser`, and saw it in the list with the input cleared.
- A fresh API container without mounted secrets had no password file. Only the proxy published a host port, at `127.0.0.1:18250`. All containers had log limits of 5 MB per file and two files.
- The final web image was 62,282,542 bytes. Its Node build base was 261,346,799 bytes. The final image contains built files and nginx, without Node or build packages. This measures image contents, not faster builds or requests.
- Both package install audits reported zero advisories after the Vite correction. This was an author check and one local run, without a separate reviewer or load test.
- Removed this attempt's containers, private network, test-data volumes, and generated password after the checks.
