# Pod Basics

Source: [PlatformLab tasks](https://github.com/theplatformlab/CKA-Certified-Kubernetes-Administrator/blob/802ee2f35412242b7c64be9861f0a7feac367b9e/exercises/01-pod-basics/README.md#tasks)

## Exercise Definition

Create the requested nginx Pod, check its settings and IP, then add and remove labels. The original instructions and hints remain in [source/UPSTREAM.md](source/UPSTREAM.md).

## Solution

### Decisions, 2026-10-12

- Use the first exercise in this collection and keep it in progress until completion is explicitly chosen.
- Follow the task's `nginx:1.27`, rather than the `1.28` command in its hints. Pin the image so the run can be repeated with the same contents.
- Use the installed kind 0.31.0 to create one temporary Kubernetes 1.35.0 node in Docker Desktop. Keep the kubeconfig under ignored build output.
- Use kubectl inside that node. There is no need to install another copy on the Mac or use the home-lab setup.
- Keep the Pod settings in one YAML file. Use Kubernetes itself to check the file and running Pod, with no extra test framework.
- The first server dry run accepted the Namespace but could not check the Pod because that Namespace had not actually been created. Apply the file first, then dry-run it against the existing Namespace.

### Run from the repository root

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
pod_file=niches/code/devops/orchestration/kubernetes/cka/platformlab-exercises/01-pod-basics/pod.yaml
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

### Checks, 2026-10-12

- kind 0.31.0 created the named node. Kubernetes server and kubectl both reported 1.35.0. The node was Ready.
- The saved file created Namespace `exercise-01` and Pod `web`. A server dry run then accepted both objects.
- The Pod was Running and Ready, with zero restarts. Its initial labels were `app=web,tier=frontend`.
- Read the Pod's JSON and checked requests of `64Mi` memory and `100m` CPU, with limits of `128Mi` and `250m`.
- `-o wide` showed IP `10.244.0.5`. nginx reported 1.27.5. An HTTP request from the node returned 200 and the nginx welcome page.
- Adding `version=v1` and removing `tier` left `app=web,version=v1`. The Pod's ID stayed the same, so these were changes to the running Pod.
- This checks one local Kubernetes setup and the requested tasks. It does not test load, resource exhaustion, or a production deployment.
- Deleted the exercise Namespace and the named cluster after checking the work. No kind clusters or Docker containers remained running.
- The work and checks are recorded. Completion has not been chosen, so the lab stays `in-progress` with no completion date.

### Completion, 2026-10-12

- The later request chose completion. Recreated the same pinned kind cluster and reran the saved Pod file.
- Server dry run, Ready wait, exact labels and resource values, unchanged Pod ID after label edits, and the HTTP 200 nginx page all passed again.
- The Pod again had IP `10.244.0.5`, zero restarts, and nginx 1.27.5. Removed the Namespace and named cluster afterward.
- Marked this attempt complete. The earlier note above records why it had stayed in progress.
