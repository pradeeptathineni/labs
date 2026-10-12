#!/usr/bin/env python3

# 26-service-discovery/check.py - Check live discovery and failed dependencies
# Usage: python3 check.py (after docker compose up --wait)

# Use built-in tools for HTTP requests, timestamps, and Compose
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.request

# Keep all changes inside this lab's Compose project
HERE = Path(__file__).resolve().parent
BASE = "http://127.0.0.1:18260"


# Read successful and failed JSON responses
def request(path):
    try:
        response = urllib.request.urlopen(BASE + path, timeout=6)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        return response.status, json.load(response)


# Wait for an expected status and optional error body after a state change
def expect(path, status, error=None):
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        try:
            actual, body = request(path)
            if actual == status and (error is None or body.get("error") == error):
                return body
        except (OSError, urllib.error.URLError):
            pass
        time.sleep(1)
    raise AssertionError(f"{path} did not return {status} and {error!r}")


# Control only the services in this Compose file
def compose(*args):
    subprocess.run(["docker", "compose", *args], cwd=HERE, check=True)


# Check routes and prove that the gateway depends on the registry
def main():
    for key in ("a", "b", "c"):
        body = expect(f"/{key}/info", 200)
        assert body["service"] == f"service-{key}"
        stamp = datetime.fromisoformat(body["timestamp"])
        assert stamp.tzinfo is not None
        assert abs((datetime.now(timezone.utc) - stamp).total_seconds()) < 10
    assert request("/unknown/info")[0] == 404
    print("PASS: three discovered routes, fresh UTC timestamps, unknown route", flush=True)

    # Crash one service so Consul must detect its failed HTTP health check
    compose("kill", "--signal", "SIGKILL", "service-b")
    try:
        expect("/b/info", 503, "No healthy service")
        saved = subprocess.check_output([
            "docker", "compose", "exec", "-T", "gateway", "python", "-c",
            "import app,json; print(json.dumps(app.registry('/health/service/service-b')))",
        ], cwd=HERE)
        instances = json.loads(saved)
        assert instances and any(
            check["Status"] == "critical" for check in instances[0]["Checks"]
        )
        expect("/a/info", 200)
        expect("/c/info", 200)
    finally:
        compose("start", "service-b")
        expect("/b/info", 200)
    print("PASS: crashed service remains registered but is excluded, then recovers", flush=True)

    # Recreate the in-memory registry to prove services register again
    compose("stop", "consul")
    try:
        expect("/a/info", 503, "Dependency unavailable")
        expect("/health", 503)
    finally:
        compose("up", "-d", "--no-deps", "--force-recreate", "consul")
        for key in ("a", "b", "c"):
            expect(f"/{key}/info", 200)
    print("PASS: registry outage has no fallback, all services register again", flush=True)


# Exit with a visible failure when a check does not hold
if __name__ == "__main__":
    main()
