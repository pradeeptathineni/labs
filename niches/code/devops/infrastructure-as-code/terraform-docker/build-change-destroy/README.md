# Build, Change, and Destroy Local Infrastructure

Source: [HashiCorp Developer Tutorials](https://developer.hashicorp.com/terraform/tutorials/docker-get-started)

## Problem

Manage a local Docker container through Terraform plans, state, updates, and teardown.

Follow the linked exercise for its requirements. The checks below define what I want to verify in my attempt; extensions are my additions.

## Before starting

Terraform CLI and a Docker engine. Follow the collection’s Build, Change, and Destroy tutorials as one lifecycle; inspect the provider endpoint for the local engine. Keep .terraform/, state, saved plans, and credentials out of public notes.

## Checks

- Capture a create plan and the served HTTP response, then verify a second plan has no changes.
- Change the external port and explain the update or replacement shown by the plan.
- Compare the resource addresses in state before and after the change.
- Review and apply the destroy plan; verify the managed container is absent.
