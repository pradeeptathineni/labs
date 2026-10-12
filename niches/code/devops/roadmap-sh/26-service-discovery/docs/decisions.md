# Discovery notes

## 2026-10-12

- Used Compose for Consul, three services, and a gateway. Only the gateway exposes a loopback port.
- Python's built-in HTTP server and client were enough for the JSON services.
- Services register with an HTTP health check through the [agent service API](https://developer.hashicorp.com/consul/api-docs/agent/service).
  - The gateway asks the [health API](https://developer.hashicorp.com/consul/api-docs/health) for `passing=true` services, then uses the returned address.
  - Repeat registration every five seconds. Consul's development registry loses its in-memory state on recreation.
- The first live check passed routes, UTC timestamps, unknown routes, shutdown and restart, and registry recreation.
  - Review found that graceful shutdown deregisters a service. It had not tested crash detection.
  - Changed the check to SIGKILL service-b.
    - Registration stayed present with a critical health check.
    - The gateway returned `No healthy service` for b, while a and c kept working.
    - Restarting b restored its route.

## Local results

- Docker Desktop 4.92.0, Engine 29.8.0, Compose 5.5.1, Python 3.12.14, Consul 1.22.7. Base images pinned by digest, no extra Python packages.
- Python syntax checks and `python3 check.py` passed.
  - All three service names, fresh UTC timestamps, unknown-route 404, crash detection, and recovery.
  - Stopping Consul returned 503. Recreating its empty registry restored all three routes through repeated registration.
- All five containers became healthy.
  - Python containers ran as user 65532.
  - Only `127.0.0.1:18260` was published. Logs used two 5 MB files per container.
- One local setup. No load test or multi-node Consul check.
- Removed the five containers, network, and temporary volumes afterward.
