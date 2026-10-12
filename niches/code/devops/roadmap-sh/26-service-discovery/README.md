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
