import os
import json
import urllib.request
import urllib.parse
from datetime import datetime

print("Runbook triggered via webhook")
print(f"Trigger time (UTC): {datetime.utcnow()}")

# CONFIGURATION
SUBSCRIPTION_ID = "113c5c83-9030-48a2-b8b8-e9587039c1f7"
RESOURCE_GROUP = "KalpanaRG"
VM_NAME = "VM1"

# GET ACCESS TOKEN USING MANAGED IDENTITY
def get_access_token():
    endpoint = os.environ.get("IDENTITY_ENDPOINT")
    header = os.environ.get("IDENTITY_HEADER")

    params = urllib.parse.urlencode({
        "resource": "https://management.azure.com/"
    })

    url = f"{endpoint}?{params}"

    req = urllib.request.Request(url)
    req.add_header("X-IDENTITY-HEADER", header)
    req.add_header("Metadata", "true")

    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())

    return data["access_token"]

# STOP SINGLE VM
def stop_vm(token):
    url = (
        f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}"
        f"/resourceGroups/{RESOURCE_GROUP}"
        f"/providers/Microsoft.Compute/virtualMachines/{VM_NAME}"
        f"/deallocate?api-version=2024-11-01"
    )

    req = urllib.request.Request(url, method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")

    with urllib.request.urlopen(req) as response:
        response.read()

    print(f"Stopping VM: {VM_NAME}")

# MAIN
def main():
    token = get_access_token()
    stop_vm(token)
    print("VM stopped successfully.")

main()
