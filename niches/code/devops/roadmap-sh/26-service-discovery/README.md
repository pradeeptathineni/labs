# Service Discovery

## Exercise definition

[Service Discovery on roadmap.sh](https://roadmap.sh/projects/service-discovery)

## Solution

Three Python services register with Consul. A gateway discovers healthy addresses on each request. From this lab folder, with Docker Desktop and Python 3:

```bash
# Build and start only this lab's five containers
docker compose up --build --wait --wait-timeout 120

# Fetch each service through the gateway
curl --fail http://127.0.0.1:18260/a/info
curl --fail http://127.0.0.1:18260/b/info
curl --fail http://127.0.0.1:18260/c/info

# Check routes, a crashed service, and a recreated registry
python3 check.py
docker compose ps
docker compose logs --tail 20

# Remove this lab's containers, network, and temporary volumes
docker compose down --volumes
```

- Routes: `/a/info`, `/b/info`, `/c/info`, and `/health`.
  - Unknown paths return 404.
  - Missing healthy services or failed dependencies return 503 with a JSON error.
- `check.py` kills service-b, restarts it, and recreates Consul.
- Only the gateway publishes a port, at `127.0.0.1:18260`. Consul runs in development mode, without ACLs or TLS.
- One instance per service, without load balancing or retries. Health checks run every two seconds, so a crash can fail a request before Consul marks it unhealthy.

[Registration choices and checks](docs/decisions.md)
