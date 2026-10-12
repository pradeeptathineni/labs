#!/usr/bin/env python3

# src/app.py - Register a service or route through Consul
# Usage: SERVICE_NAME=service-a python3 src/app.py, or ROLE=gateway python3 src/app.py

# Use built-in HTTP tools, threads, and UTC timestamps
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
import signal
import threading
import urllib.error
import urllib.request

# Keep the lab's names and registry separate from request input
CONSUL = "http://consul:8500/v1"
NAMES = {"a": "service-a", "b": "service-b", "c": "service-c"}
ROLE = os.environ.get("ROLE", "service")
NAME = os.environ.get("SERVICE_NAME", "")
STOP = threading.Event()


# Read JSON or send a registration with a short request timeout
def registry(path, body=None):
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        CONSUL + path,
        data=data,
        method="GET" if body is None else "PUT",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=2) as response:
        value = response.read()
        return json.loads(value) if value else None


# Restore this registration after a registry restart
def register():
    payload = {
        "ID": NAME,
        "Name": NAME,
        "Address": NAME,
        "Port": 8000,
        "Check": {
            "HTTP": f"http://{NAME}:8000/health",
            "Interval": "2s",
            "Timeout": "1s",
        },
    }
    while not STOP.is_set():
        try:
            registry("/agent/service/register", payload)
        except (OSError, urllib.error.URLError, ValueError):
            print("Registration unavailable; retrying", flush=True)
        STOP.wait(5)


# Serve fixed JSON routes and hide dependency exception details
class Handler(BaseHTTPRequestHandler):
    # Write one complete JSON response
    def reply(self, status, body):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    # Use the service's local route or the gateway's discovery route
    def do_GET(self):
        try:
            if self.path == "/health":
                if ROLE == "gateway" and not registry("/status/leader"):
                    return self.reply(503, {"error": "No registry leader"})
                return self.reply(200, {"ready": True})

            # Each dummy service supplies its name and a fresh UTC timestamp
            if ROLE == "service":
                if self.path != "/info":
                    return self.reply(404, {"error": "Unknown route"})
                return self.reply(200, {
                    "service": NAME,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                })

            # Accept only the three known routes, then query passing instances
            routes = {f"/{key}/info": value for key, value in NAMES.items()}
            name = routes.get(self.path)
            if name is None:
                return self.reply(404, {"error": "Unknown route"})
            instances = registry(f"/health/service/{name}?passing=true")
            if not instances:
                return self.reply(503, {"error": "No healthy service"})

            # Use the address returned by Consul rather than a fallback host
            service = instances[0]["Service"]
            url = f"http://{service['Address']}:{service['Port']}/info"
            with urllib.request.urlopen(url, timeout=2) as response:
                body = json.load(response)
            self.reply(200, body)
        except (OSError, urllib.error.URLError, ValueError, KeyError):
            self.reply(503, {"error": "Dependency unavailable"})


# Start HTTP before registration, then stop cleanly on a container signal
def main():
    if ROLE not in ("service", "gateway"):
        raise ValueError("Unknown role")
    if ROLE == "service" and NAME not in NAMES.values():
        raise ValueError("Unknown service name")
    server = ThreadingHTTPServer(("0.0.0.0", 8000), Handler)
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    registration = None
    if ROLE == "service":
        registration = threading.Thread(target=register, daemon=True)
        registration.start()

    # Let the main thread handle signals without blocking the HTTP worker
    signal.signal(signal.SIGTERM, lambda *_: STOP.set())
    signal.signal(signal.SIGINT, lambda *_: STOP.set())
    STOP.wait()
    if registration is not None:
        registration.join(timeout=3)
        try:
            registry(f"/agent/service/deregister/{NAME}", {})
        except (OSError, urllib.error.URLError, ValueError):
            pass
    server.shutdown()
    server.server_close()
    worker.join(timeout=3)


# Run the selected role
if __name__ == "__main__":
    main()
