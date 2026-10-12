# Service Discovery

Source: [roadmap.sh](https://roadmap.sh/projects/service-discovery)

## Exercise Definition

Read the [original exercise definition](https://roadmap.sh/projects/service-discovery).

## Solution

### Starting choices, 2026-10-12

- This was the second random pick from Blue-Green Deployment, Multi-Service Application, and Service Discovery. Complete its required work locally, without a cloud account.
- Run Consul, three small services, and a gateway in Compose. Only the gateway opens a loopback port. Consul's development mode is enough for this attempt.
- Use Python's HTTP server and HTTP client for the small JSON services. No web framework or new package is needed.
- Each service registers itself with Consul and supplies an HTTP health check. The gateway asks Consul for passing services on each request, then calls the returned address.
- Repeat registration every five seconds so services recover when the development registry loses its in-memory state.
- Finish after checking all three routes, real timestamps, unknown routes, a stopped service, registry failure, recovery, and cleanup. This does not test a production Consul cluster.

### First run

- The first live check passed all three routes, current UTC timestamps, unknown-route handling, service stop and restart, and registration after Consul was recreated.
- Reviewing that check showed a gap: graceful service shutdown removes its registration. It checks deregistration, not Consul marking a crashed service unhealthy. Add a forced crash check before completion.
- Changed the check to send SIGKILL to service-b. It then confirmed that Consul kept the registration with a critical health check and the gateway returned `No healthy service`. The corrected check passed.

### Run

```bash
cd niches/code/devops/roadmap-sh/26-service-discovery

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

- `check.py` kills one dummy service, starts it again, and recreates Consul. Run it only against this lab.
- Registration uses Consul's [agent service API](https://developer.hashicorp.com/consul/api-docs/agent/service). Discovery uses the [health API](https://developer.hashicorp.com/consul/api-docs/health) with `passing=true`.
- The gateway accepts `/a/info`, `/b/info`, `/c/info`, and `/health`. Unknown paths return 404. Missing healthy services and failed dependencies return 503 with a short JSON error.
- Checks run every two seconds. A crash can still cause a request failure before Consul marks it critical. There is one instance per name, without load balancing or retrying another instance.
- Consul development state is temporary. This setup has no ACLs, TLS, or multiple registry nodes. The gateway listens only on loopback, and the registry and service ports stay inside Docker.

### Checks, 2026-10-12

- Docker Desktop 4.92.0, Engine 29.8.0, Compose 5.5.1, Python 3.12.14, and Consul 1.22.7 ran this attempt. Base images are pinned by digest. No Python packages were installed.
- `python3 -m py_compile app.py check.py` passed. The live check then passed all three service names, fresh UTC timestamps, and unknown-route 404 handling.
- A forced service-b crash left its registration present with a critical check. `/b/info` returned 503 with `No healthy service`, while a and c still worked. Starting b restored its route.
- Stopping Consul caused 503 responses from the gateway. Recreating the empty registry restored all three routes through repeated self-registration. There was no hardcoded address fallback.
- All five containers became healthy. The Python containers ran as user 65532. Only `127.0.0.1:18260` was published, and logs used 5 MB files with a two-file limit.
- This was an author check on one local setup. It does not establish production reliability, load capacity, or user experience.
