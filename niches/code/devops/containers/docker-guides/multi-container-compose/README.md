# Multi-container Application with Docker Compose

Source: [Docker Hands-on Guides](https://docs.docker.com/get-started/docker-concepts/running-containers/multi-container-applications/)

## Exercise definition

Run the same proxy, web, and Redis stack manually and with Compose; compare behavior.

Follow the linked exercise for its requirements. The checks below define what I want to verify in my attempt; extensions are my additions.

## Before starting

A Docker engine and Compose v2, Git, and a free local HTTP port. Fetch the sample through the source link; record its commit and image versions when attempting it. Keep upstream files outside personal solution notes.

## Checks

- Show requests reaching both web containers and the shared visit counter increasing.
- Compare the manual network/aliases with Compose’s service networking and rendered configuration.
- Extension: stop Redis, capture the failure, then restore it and verify requests work again.
- Remove only this stack’s containers and network; record what happened to its data.

## Solution

## Takeaways

## Applications
