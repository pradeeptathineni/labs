# CKS objectives review

Source material: [CNCF CKS](https://www.cncf.io/training/certification/cks/) · [curriculum snapshot](https://github.com/cncf/curriculum/blob/88e610650e2edbe04325fcb992febe6838487d72/CKS_Curriculum%20v1.34.pdf)

## Exercise Definition

This is a locally designed review based on `CKS_Curriculum v1.34.pdf` at curriculum revision `88e610650e2edbe04325fcb992febe6838487d72`, inspected on 2026-10-05. These 6 prompts sample the published objectives; they are not official exam questions or a complete syllabus assessment.

For each prompt, explain your choices, identify useful evidence and cite the relevant official references. Record uncertainties alongside the answer. This set requires explanation; practical execution belongs in the code labs.

The pinned CKS PDF and its repository README give different domain weights. This review uses the PDF objectives and makes no scoring or weighting claim.

1. **Cluster setup.** Review a proposed cluster with a public ingress, a cloud metadata endpoint and node components installed from downloaded binaries. Explain which trust, TLS, network-policy and benchmark checks you would prioritize and what evidence would satisfy each check.

2. **Cluster hardening.** Compare the access granted to a human administrator and an application service account. Explain how you would reduce API exposure and unnecessary permissions, review default account use, and decide whether a Kubernetes upgrade is needed.

3. **System hardening.** Explain how host attack surface, external network access, least privilege, seccomp and AppArmor address different risks. Identify a compatibility concern and a verification method for each proposed restriction.

4. **Microservice vulnerabilities.** Compare pod security standards, secret handling, workload isolation and Pod-to-Pod encryption. Explain which threats each addresses and which remain when an application itself has a vulnerability.

5. **Supply chain security.** Trace an image from source and CI through a registry into a cluster. Explain where an SBOM, static analysis, smaller base images, artifact signatures and permitted registries help, and what each fails to prove on its own.

6. **Monitoring, logging and runtime security.** A running container performs an unexpected action. Outline the evidence you would preserve from runtime behavior, audit logs, workloads and network activity. Explain how you would distinguish an application fault from suspicious activity and test a containment proposal without losing the evidence.

## Solution
