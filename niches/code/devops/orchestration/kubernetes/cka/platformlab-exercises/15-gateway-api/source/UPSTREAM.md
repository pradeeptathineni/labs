# Upstream material — ThePlatformLab

Source: [exercises/15-gateway-api/README.md](https://github.com/theplatformlab/CKA-Certified-Kubernetes-Administrator/blob/802ee2f35412242b7c64be9861f0a7feac367b9e/exercises/15-gateway-api/README.md) · revision `802ee2f35412242b7c64be9861f0a7feac367b9e`

> [!IMPORTANT]
> This is upstream material, re-rendered only to pin its links. Hints, reference answers, verification examples and first-person anecdotes belong to the original author. They are not my Solution or my experience. See [the original MIT notice](LICENSE.txt).

---

# Exercise 15 — Gateway API: Gateway and HTTPRoute

> **Medium** | ~20 min | Domain: Services & Networking (20%)
>
> Related: [Gateway API skeleton](https://github.com/theplatformlab/CKA-Certified-Kubernetes-Administrator/blob/802ee2f35412242b7c64be9861f0a7feac367b9e/skeletons/gateway-api.yaml) | [README — Services & Networking](https://github.com/theplatformlab/CKA-Certified-Kubernetes-Administrator/blob/802ee2f35412242b7c64be9861f0a7feac367b9e/README.md#domain-5--services--networking-20)

Gateway API is GA in v1.35 and replaces classic Ingress for modern traffic management. Set up a Gateway and route HTTP traffic to a backend service.

## Tasks

1. Create a namespace called `exercise-15`
1. Verify a GatewayClass exists in the cluster (depends on your CNI/controller)
1. Create a Gateway named `web-gateway` in namespace `exercise-15`:
   - Reference the existing GatewayClass
   - Listen on port 80, protocol HTTP
1. Create a Deployment named `web` with image `nginx:1.28` and 2 replicas
1. Expose it with a ClusterIP Service named `web-svc` on port 80
1. Create an HTTPRoute named `web-route` that:
   - References `web-gateway` as the parent
   - Matches path prefix `/`
   - Routes to `web-svc` on port 80
1. Verify the Gateway status shows `Programmed: True`
1. Verify the HTTPRoute is attached to the Gateway

## Hints

<details>
<summary>Stuck? Click to reveal hints</summary>

- `k get gatewayclass` to find the available class
- The Gateway `listeners[].protocol` is `HTTP`, not `TCP`
- HTTPRoute `parentRefs` must match the Gateway name and namespace
- Check status: `k get gateway web-gateway -n exercise-15 -o yaml`
- If no GatewayClass is installed, use Envoy Gateway or Cilium

</details>

## What tripped me up

> The `parentRefs.name` in HTTPRoute must match the Gateway name EXACTLY. I had `web-gw` in the HTTPRoute but the Gateway was called `web-gateway`. No error — the HTTPRoute just never attached to anything. Traffic goes nowhere and there's no obvious indication why. I spent 10 minutes checking backend pods and service selectors when the problem was a one-word typo in parentRefs.
>
> Also: Gateway API won't work without a GatewayClass controller actually installed. On a fresh cluster there might be no GatewayClass at all. `k get gatewayclass` — if it's empty, you need to install a controller first. The exam environment should have one, but verify before writing YAML.

## Verify

```bash
# Gateway ready
k get gateway web-gateway -n exercise-15

# HTTPRoute accepted
k get httproute web-route -n exercise-15

# Backend pods running
k get pods -n exercise-15
```

## Cleanup

```bash
k delete ns exercise-15
```

<details>
<summary>Solution</summary>

```bash
k create ns exercise-15

# Check GatewayClass
k get gatewayclass
# Note the name, e.g., "eg" for Envoy Gateway or "cilium" for Cilium
```

```yaml
# gateway.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: web-gateway
  namespace: exercise-15
spec:
  gatewayClassName: eg    # replace with your GatewayClass name
  listeners:
  - name: http
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: Same
```

```bash
# Deploy backend
k create deployment web -n exercise-15 --image=nginx:1.28 --replicas=2
k expose deployment web -n exercise-15 --port=80 --target-port=80 --name=web-svc
```

```yaml
# httproute.yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: web-route
  namespace: exercise-15
spec:
  parentRefs:
  - name: web-gateway
    namespace: exercise-15
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: web-svc
      port: 80
```

```bash
k apply -f gateway.yaml
k apply -f httproute.yaml

# Check Gateway status
k get gateway web-gateway -n exercise-15
k get gateway web-gateway -n exercise-15 -o yaml | grep -A5 "conditions"

# Check HTTPRoute
k get httproute web-route -n exercise-15 -o yaml | grep -A5 "parents"
```

</details>
