# Pod Basics

## Exercise definition

[PlatformLab tasks](https://github.com/theplatformlab/CKA-Certified-Kubernetes-Administrator/blob/802ee2f35412242b7c64be9861f0a7feac367b9e/exercises/01-pod-basics/README.md#tasks) · [Saved instructions and hints](source/UPSTREAM.md)

Create an nginx Pod, inspect its settings and IP, then add and remove labels.

## Solution

[src/pod.yaml](src/pod.yaml) creates Namespace `exercise-01` and Pod `web`.

- nginx 1.27, pinned by digest.
- Initial labels: `app=web,tier=frontend`.
- Requests: `64Mi` memory and `100m` CPU. Limits: `128Mi` and `250m`.

[Run with kind](docs/run.md) · [Decisions and results](docs/decisions.md)
