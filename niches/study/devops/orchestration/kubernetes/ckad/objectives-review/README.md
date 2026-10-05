# CKAD objectives review

Source material: [CNCF CKAD](https://www.cncf.io/training/certification/ckad/) · [curriculum snapshot](https://github.com/cncf/curriculum/blob/88e610650e2edbe04325fcb992febe6838487d72/CKAD_Curriculum_v1.37.pdf)

## Exercise Definition

This is a locally designed review based on `CKAD_Curriculum_v1.37.pdf` at curriculum revision `88e610650e2edbe04325fcb992febe6838487d72`, inspected on 2026-10-05. These 5 prompts sample the published objectives; they are not official exam questions or a complete syllabus assessment.

For each prompt, explain your choices, identify useful evidence and cite the relevant official references. Record uncertainties alongside the answer. This set requires explanation; practical execution belongs in the code labs.

1. **Application design and build.** Choose workload resources for a continuous API, a scheduled batch job and a node-local collector. Compare init containers and sidecars, and explain when their data should use ephemeral or persistent storage. Identify the container-image assumptions that affect those choices.

2. **Application deployment.** Compare rolling, canary and blue/green deployment for a stateful user-facing service. Explain the responsibilities of Kubernetes resources, Helm and Kustomize in your chosen approach, including rollback and API-version compatibility checks.

3. **Application observability and maintenance.** An application starts slowly and occasionally stops responding. Distinguish startup, readiness and liveness probes. Explain which logs, status and CLI observations would support each diagnosis and how an unsuitable probe could make the situation worse.

4. **Application environment, configuration and security.** Describe how configuration, secrets, service accounts, authorization, admission controls and resource quotas affect a deployed application. Compare a standard resource with an operator-managed resource, and explain how you would find the applicable security constraints.

5. **Services and networking.** An application works inside its Pod but cannot be reached by a client. Explain how you would investigate its Service, selectors, ports, network policies and Ingress rules. Distinguish exposing an endpoint from authorizing traffic to it.

## Solution
