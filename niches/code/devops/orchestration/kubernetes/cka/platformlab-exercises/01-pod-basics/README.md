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
