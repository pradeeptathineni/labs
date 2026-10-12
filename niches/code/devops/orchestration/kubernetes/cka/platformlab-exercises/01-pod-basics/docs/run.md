# Temporary kind cluster

From the repository root, with kind and Docker Desktop:

```bash
# Create only this exercise's cluster and keep its settings separate
mkdir -p .meta/build/pod-basics
kind create cluster \
    --name labs-pod-basics \
    --image kindest/node:v1.35.0@sha256:452d707d4862f52530247495d180205e029056831160e22870e37e3f6c1ac31f \
    --kubeconfig .meta/build/pod-basics/kubeconfig \
    --wait 120s

# Use kubectl from the node without changing the host's current context
k() {
    docker exec -i labs-pod-basics-control-plane kubectl \
        --kubeconfig=/etc/kubernetes/admin.conf "$@"
}

# Create both objects and wait for the Pod to be ready
pod_file=niches/code/devops/orchestration/kubernetes/cka/platformlab-exercises/01-pod-basics/src/pod.yaml
k apply -f - < "$pod_file"
k wait -n exercise-01 --for=condition=Ready pod/web --timeout=120s

# Check the file against the server now that the Namespace exists
k apply --dry-run=server -f - < "$pod_file"
k get pod web -n exercise-01 -o wide --show-labels
k get pod web -n exercise-01 -o jsonpath='{.spec.containers[0].resources}'
printf '\n'

# Change the running Pod's labels and inspect them again
k label pod web -n exercise-01 version=v1
k label pod web -n exercise-01 tier-
k get pod web -n exercise-01 --show-labels

# Check the nginx version and reach the Pod from its node
k exec web -n exercise-01 -- nginx -v
pod_address=$(k get pod web -n exercise-01 -o jsonpath='{.status.podIP}')
docker exec labs-pod-basics-control-plane curl \
    --fail --silent --show-error --max-time 5 "http://$pod_address/"

# Remove only the exercise's Namespace and named cluster when finished
k delete namespace exercise-01 --wait=true --timeout=60s
kind delete cluster --name labs-pod-basics
unset -f k
```
