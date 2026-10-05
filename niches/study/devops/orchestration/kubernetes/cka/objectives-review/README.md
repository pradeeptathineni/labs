# CKA objectives review

Source material: [CNCF CKA](https://www.cncf.io/training/certification/cka/) · [curriculum snapshot](https://github.com/cncf/curriculum/blob/88e610650e2edbe04325fcb992febe6838487d72/CKA_Curriculum_v1.35.pdf)

## Exercise Definition

This is a locally designed review based on `CKA_Curriculum_v1.35.pdf` at curriculum revision `88e610650e2edbe04325fcb992febe6838487d72`, inspected on 2026-10-05. These 5 prompts sample the published objectives; they are not official exam questions or a complete syllabus assessment.

For each prompt, explain your choices, identify useful evidence and cite the relevant official references. Record uncertainties alongside the answer. This set requires explanation; practical execution belongs in the code labs.

1. **Cluster architecture, installation and configuration.** Compare the responsibilities of the control plane and worker nodes. Explain what changes when the control plane must remain available through one node failure, what to check before an upgrade, and where RBAC, CNI, CSI and CRI fit into administration.

2. **Workloads and scheduling.** A Deployment has Pending Pods, and a later rollout produces crashing Pods. Explain how you would distinguish scheduling constraints, resource shortages and application configuration problems. Describe the evidence needed before changing scaling settings or rolling back.

3. **Services and networking.** An application is reachable from one Pod but not through its public entry point. Trace the possible roles of selectors, endpoints, DNS, network policy, Services, Ingress and Gateway API. Choose an order for diagnosis and explain what each observation would rule out.

4. **Storage.** Compare persistent volumes, claims and storage classes, including dynamic provisioning, access modes and reclaim policies. Explain the consequences of deleting a workload or a claim when its data must survive.

5. **Troubleshooting.** A node becomes NotReady while several applications are slow. Describe how you would separate a node or cluster-component problem from workload pressure. Identify the logs, events and resource measurements you would collect before proposing a change.

## Solution
