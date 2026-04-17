import json
import urllib.request
import time

BASE_URL = "https://mud4ai.interaction.tw/a2a"

def try_method(method, params={}):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": "1",
        "params": params
    }
    print(f"--- Trying Method: {method} ---")
    try:
        req = urllib.request.Request(
            BASE_URL,
            data=json.dumps(payload).encode('utf-8'),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode('utf-8'))
            if "error" in data:
                print(f"Error: {data['error'].get('message')}")
            else:
                print(f"Success: {json.dumps(data.get('result'))[:200]}...")
            return data
    except Exception as e:
        print(f"Connection Error: {e}")
        return None

if __name__ == "__main__":
    try_method("ListMethods")
    try_method("GetTask", {"taskId": "dummy"})
    try_method("ListMessages", {"taskId": "dummy"})
    try_method("GetSystemStatus")
