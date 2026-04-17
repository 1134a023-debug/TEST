import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"

def a2a_send(action, task_id=None):
    msg = {"messageId": f"msg-{id(action)}", "role": "user",
           "parts": [{"kind": "text", "text": json.dumps(action)}]}
    if task_id:
        msg["taskId"] = task_id
    
    req = urllib.request.Request(
        "https://mud4ai.interaction.tw/a2a",
        data=json.dumps({
            "jsonrpc": "2.0", "method": "SendMessage", "id": "1",
            "params": {"message": msg}
        }).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    res = urllib.request.urlopen(req, timeout=15)
    return json.loads(res.read().decode('utf-8')).get("result", {}).get("task", {})

def print_artifacts(task_obj):
    if "artifacts" in task_obj:
        for art in task_obj["artifacts"]:
            for part in art.get("parts", []):
                print(part.get("text", ""))

if __name__ == "__main__":
    print("[MASTER] Connecting via A2A...", flush=True)
    task = a2a_send({"action": "join", "params": {"player_name": "無限", "token": MASTER_TOKEN}})
    task_id = task.get("id")
    if not task_id:
        print("[MASTER] Failed to get task_id!")
        sys.exit(1)
        
    print_artifacts(task)
    
    print("\n[MASTER] Fetching Status Panel...", flush=True)
    status_task = a2a_send({"action": "get_status"}, task_id)
    print_artifacts(status_task)
