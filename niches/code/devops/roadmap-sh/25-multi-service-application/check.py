#!/usr/bin/env python3

# 25-multi-service-application/check.py - Check the running stack and recovery
# Usage: python3 check.py (after docker compose up --wait)

# Use the standard library for HTTP checks and Compose commands
import json
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.request
import uuid

# Run only this lab's Compose project
HERE = Path(__file__).resolve().parent
BASE = "http://127.0.0.1:18250"


# Read both successful and failed responses without hiding their status
def request(path, body=None):
    data = None if body is None else body.encode()
    req = urllib.request.Request(
        BASE + path, data=data, headers={"Content-Type": "application/json"}
    )
    try:
        response = urllib.request.urlopen(req, timeout=8)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        return response.status, response.headers, response.read().decode()


# Wait briefly for store connections to recover
def ready():
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        try:
            if request("/api/health")[0] == 200:
                return
        except (OSError, urllib.error.URLError):
            pass
        time.sleep(1)
    raise AssertionError("API did not recover within 45 seconds")


# Stop and start only services owned by this lab
def compose(*args):
    subprocess.run(["docker", "compose", *args], cwd=HERE, check=True)


# Check input handling, cached reads, persistence, and failed stores
def main():
    ready()
    status, _, page = request("/")
    assert status == 200 and "Lab notes" in page and "/assets/" in page
    assert request("/api/notes", '{"title":" "}')[0] == 400
    assert request("/api/notes", "{")[0] == 400
    assert request("/api/notes", json.dumps({"title": "x" * 201}))[0] == 400

    # A write must clear the cache, then a second read must hit it
    title = "check-" + uuid.uuid4().hex
    assert request("/api/notes", json.dumps({"title": title}))[0] == 201
    status, headers, body = request("/api/notes")
    assert status == 200 and headers["X-Cache"] == "miss"
    assert any(row["title"] == title for row in json.loads(body))
    assert request("/api/notes")[1]["X-Cache"] == "hit"
    print("PASS: page, bad input, write, cache miss and cache hit", flush=True)

    # Recreate containers while keeping named volumes and verify the saved note
    compose("down")
    compose("up", "--wait", "--wait-timeout", "120")
    ready()
    assert any(row["title"] == title for row in json.loads(request("/api/notes")[2]))
    print("PASS: data survived container removal and recreation", flush=True)

    # Each stopped dependency must fail safely and recover after restart
    for service in ("redis", "mongo"):
        compose("stop", service)
        try:
            assert request("/api/health")[0] == 503
            assert request("/api/notes", '{"title":"outage"}')[0] == 503
        finally:
            compose("start", service)
            ready()
        print(f"PASS: {service} outage and recovery", flush=True)


# Keep failures visible to the shell
if __name__ == "__main__":
    main()
