# User Role Controlled by Request Parameter

Source: [PortSwigger Web Security Academy](https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter)

## Problem

Investigate client-controlled authorization and explain a server-side fix in a hosted lab.

Follow the linked exercise for its requirements. The checks below define what I want to verify in my attempt; extensions are my additions.

## Before starting

A free Academy account and the hosted lab instance; a browser and optionally Burp Suite Community Edition. Use the lab’s own test accounts and target. Keep temporary credentials and session cookies out of saved notes.

## Checks

- Record the ordinary-user behavior, changed request, and resulting authorization behavior.
- Complete the hosted objective and save the platform’s solved result when actually attempted.
- Explain the trust boundary and propose a server-side authorization check; label the proposal as untested unless implemented.
