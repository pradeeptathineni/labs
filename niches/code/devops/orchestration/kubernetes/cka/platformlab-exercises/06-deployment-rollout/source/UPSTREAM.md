# Upstream material — ThePlatformLab

Source: [exercises/06-deployment-rollout/README.md](https://github.com/theplatformlab/CKA-Certified-Kubernetes-Administrator/blob/802ee2f35412242b7c64be9861f0a7feac367b9e/exercises/06-deployment-rollout/README.md) · revision `802ee2f35412242b7c64be9861f0a7feac367b9e`

> [!IMPORTANT]
> This is upstream material, re-rendered only to pin its links. Hints, reference answers, verification examples and first-person anecdotes belong to the original author. They are not my Solution or my experience. See [the original MIT notice](LICENSE.txt).

---

# Exercise 06 — Deployment Rolling Update and Rollback

> Related: [Deployment skeleton](https://github.com/theplatformlab/CKA-Certified-Kubernetes-Administrator/blob/802ee2f35412242b7c64be9861f0a7feac367b9e/skeletons/deployment.yaml) | [README — Workloads & Scheduling](https://github.com/theplatformlab/CKA-Certified-Kubernetes-Administrator/blob/802ee2f35412242b7c64be9861f0a7feac367b9e/README.md#domain-3--workloads--scheduling-15)

Create a Deployment, perform a rolling update, check rollout history, and rollback.

## Tasks

1. Create a namespace called `exercise-06`
1. Create a Deployment named `webapp` with:
   - 3 replicas
   - Image: `nginx:1.28`
   - Strategy: RollingUpdate with maxSurge=1, maxUnavailable=0
   - Record the change cause
1. Verify all 3 replicas are running
1. Update the image to `nginx:1.29` and record the change
1. Watch the rollout status
1. Check rollout history — you should see 2 revisions
1. Rollback to the previous version (nginx:1.28)
1. Verify the rollback worked by checking the image

## Hints

<details>
<summary>Stuck? Click to reveal hints</summary>

- `k create deployment webapp --image=nginx:1.28 --replicas=3`
- `k set image deployment/webapp` to update
- `k rollout status`, `k rollout history`, `k rollout undo`
- Annotate with `kubernetes.io/change-cause` to track changes in rollout history

</details>

## What tripped me up

> I used `--record` on every deployment command because that's what older guides taught. It's deprecated and removed in v1.35 — the CHANGE-CAUSE column shows `<none>`. The correct way: annotate the deployment with `kubernetes.io/change-cause` after each change. It's one extra command but it actually works.
>
> Also: I forgot that `k rollout undo` creates a NEW revision, not a revert. After undo, I had revision 1, 3 (not 1, 2). My history looked weird and I thought something broke. That's just how it works — undo creates revision N+1 with the old spec.
>
> **Why `--overwrite` on the second annotation?** The `kubernetes.io/change-cause` annotation lives on the Deployment object itself, not on individual revisions. When you update the image, the Deployment object remains the same. The old annotation persists, so you need `--overwrite` to change its value. First annotation (initial deploy) doesn't need it because the key doesn't exist yet. Second annotation (after update) needs it because the key already exists. Without `--overwrite`, the command would error with "annotation already exists".

## Verify

```bash
# After initial deploy
k get deploy webapp -n exercise-06
k get rs -n exercise-06

# After rollback — image should be nginx:1.28
k get deploy webapp -n exercise-06 -o jsonpath='{.spec.template.spec.containers[0].image}'
```

## Cleanup

```bash
k delete ns exercise-06
```

<details>
<summary>Solution</summary>

```bash
k create ns exercise-06

# Create deployment
k create deployment webapp -n exercise-06 --image=nginx:1.28 --replicas=3 $do > deploy.yaml
```

Edit `deploy.yaml` to add rolling update strategy, then apply:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  namespace: exercise-06
spec:
  replicas: 3
  selector:
    matchLabels:
      app: webapp
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: nginx
        image: nginx:1.28
```

```bash
k apply -f deploy.yaml
# First annotation — no --overwrite needed because the key doesn't exist yet
k annotate deployment webapp -n exercise-06 kubernetes.io/change-cause="initial deploy nginx:1.28"

# Verify
k get deploy webapp -n exercise-06
k get pods -n exercise-06

# Update image
k set image deployment/webapp nginx=nginx:1.29 -n exercise-06
# Second annotation — MUST use --overwrite because kubernetes.io/change-cause already exists on the Deployment object
# The annotation key lives on the Deployment, not on individual revisions, so it persists across updates
k annotate deployment webapp -n exercise-06 kubernetes.io/change-cause="update to nginx:1.29" --overwrite

# Watch rollout
k rollout status deployment/webapp -n exercise-06

# Check history
k rollout history deployment/webapp -n exercise-06

# Rollback
k rollout undo deployment/webapp -n exercise-06

# Verify rollback
k get deploy webapp -n exercise-06 -o jsonpath='{.spec.template.spec.containers[0].image}'
# Should output: nginx:1.28
```

</details>
