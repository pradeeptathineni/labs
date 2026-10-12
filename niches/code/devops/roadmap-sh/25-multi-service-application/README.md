# Multi-Service Application

## Exercise definition

[Multi-Service Application on roadmap.sh](https://roadmap.sh/projects/multiservice-docker)

## Solution

A local notes app with React, Express, MongoDB, Redis, and nginx. From this lab folder, with Docker Desktop and Python 3:

```bash
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

- Open `http://127.0.0.1:18250`. Only nginx publishes a host port.
- `check.py` creates a test note, recreates containers, and stops each store briefly.
- Keep the password file when reusing the database volume. It is ignored by Git and stored as plain text.
- Local app without authentication or TLS. MongoDB uses a lab admin account.
- Redis caches reads for ten seconds.
  - Cached reads can survive a database outage.
  - A write can be saved in MongoDB before a cache failure returns an error. Concurrent cache updates and writes are not a transaction.

[Build choices and results](docs/decisions.md)

## Takeaways

## Applications
