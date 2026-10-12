# Notes app decisions

## 2026-10-12

- Chose Compose for five local services.
  - Named volumes for saved notes, health checks for startup, and rotated logs.
  - Separate custom Node bases for API packages and the web build. Package locks and upstream image digests pin dependencies.
  - nginx serves the built React files. Node stays in the build image.
- The host npm command picked Node 16 despite a newer installation. Built in the pinned Node 24 container instead.
- The first audit found Vite 7.1.7 advisories.
  - Changed to 7.3.7 from the audit's affected-version range.
  - Both package install audits then reported zero advisories.
- MongoDB 8.0 refused Docker Desktop's Linux 7.0.12 kernel.
  - The [reported issue](https://jira.mongodb.org/browse/SERVER-121912) and [release notes](https://www.mongodb.com/docs/manual/release-notes/8.2/) cover that kernel range.
  - Used pinned MongoDB 7.0 instead of changing the host kernel or bypassing its startup check.
- [Compose secrets](https://docs.docker.com/compose/how-tos/use-secrets/) mount the password into MongoDB and the API.
  - A fresh API container without the mount had no password file.
  - The host file is plain text. Shared use would need app authentication, a restricted database account, TLS, and backups.

## Local checks

- Docker Desktop 4.92.0, Engine 29.8.0, Compose 5.5.1, Linux 7.0.12. All five services became healthy.
  - Containers: Node 24.21.0, MongoDB 7.0.43, Redis 7.4.11, nginx 1.28.3.
  - Custom bases have local tags. Rebuild them when package locks change.
- `python3 check.py` passed:
  - Served page, empty and long titles, malformed JSON, and note creation.
  - Cache miss followed by hit.
  - Saved notes after container recreation.
  - HTTP 503 during each store outage, then recovery.
- Saved `Saved through the browser` in the React page. It appeared in the list and the input cleared.
- Only the proxy published `127.0.0.1:18250`. Logs were limited to two 5 MB files per container.
- Final web image: 62,282,542 bytes. Node build base: 261,346,799 bytes.
  - The final image contains nginx and built files, without Node or build packages.
  - No build-time or request-speed measurement.
- One local run. No load test or independent review.
- Removed the containers, network, test-data volumes, and generated password afterward.
