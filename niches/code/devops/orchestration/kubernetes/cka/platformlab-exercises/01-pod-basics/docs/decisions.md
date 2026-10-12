# Pod notes

## 2026-10-12

- Used the task's `nginx:1.27`, rather than the `1.28` command in its hints. Pinned the image contents.
- Created one temporary Kubernetes 1.35.0 node with the installed kind 0.31.0 and Docker Desktop.
  - Kubeconfig under ignored build output.
  - Used kubectl inside the node, keeping the Mac's current context unchanged.
- One YAML file holds the Namespace and Pod. Checked it against Kubernetes itself.
  - The first server dry run accepted the Namespace but failed on the Pod: dry run had not created its Namespace.
  - Applied both objects, then repeated the dry run successfully.
- The node was Ready. Server and kubectl reported 1.35.0.
  - Pod Running and Ready, zero restarts, IP `10.244.0.5`.
  - Initial labels `app=web,tier=frontend`.
  - Requests `64Mi` and `100m`, limits `128Mi` and `250m`, confirmed from Pod JSON.
  - nginx reported 1.27.5. HTTP from the node returned 200 and the welcome page.
- Added `version=v1` and removed `tier`.
  - Labels became `app=web,version=v1`.
  - Pod ID stayed unchanged: these were edits to the running Pod.
- Recreated the pinned cluster and repeated the apply, dry run, Ready wait, resource and label checks, and HTTP request. All passed again with the same IP, nginx version, and zero restarts.
- Deleted the Namespace and named cluster after both runs. No kind clusters or Docker containers remained.
- Tested on this local cluster. Load and resource exhaustion were not tested.
