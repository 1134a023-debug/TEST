import urllib.request
import json
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"
MASTER_DESC = "我是一個擁有無限力量的超級強者，被稱為「無限」，掌握所有的魔法與物理技能，以及全伺服器的管理權限！"

def a2a_send(action, task_id=None):
    msg = {"messageId": f"msg-{id(action)}", "role": "user",
           "parts": [{"kind": "text", "text": json.dumps(action)}]}
    if task_id:
        msg["taskId"] = task_id
    req = urllib.request.Request(
        "https://mud4ai.interaction.tw/a2a",
        data=json.dumps({"jsonrpc": "2.0", "method": "SendMessage", "id": "1", "params": {"message": msg}}).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    res = urllib.request.urlopen(req, timeout=120)
    return json.loads(res.read().decode('utf-8')).get("result", {}).get("task", {})

def print_arts(t):
    text_content = ""
    for a in t.get("artifacts", []):
        for p in a.get("parts", []):
            t_str = p.get("text", "")
            print(t_str)
            text_content += t_str + "\n"
    return text_content

print("[MASTER] Connecting via A2A...", flush=True)
task = a2a_send({"action": "join", "params": {"player_name": "無限", "token": MASTER_TOKEN}})
task_id = task.get("id")

needs_char = False
for a in task.get("artifacts", []):
    for p in a.get("parts", []):
        if "set_character" in p.get("text", ""):
            needs_char = True

if needs_char:
    print("[MASTER] Setting character...", flush=True)
    t2 = a2a_send({"action": "set_character", "params": {"description": MASTER_DESC}}, task_id)
    time.sleep(2) 

print("\n--- STATUS PANEL ---", flush=True)
t3 = a2a_send({"action": "get_status"}, task_id)
print_arts(t3)

# Dump output to a file so it's easy to read if needed
with open("status_panel.txt", "w", encoding="utf-8") as f:
    f.write(print_arts(t3))

# After printing status, we keep the session alive by fetching status every 15s
print("\n[MASTER] Entering keep-alive loop...", flush=True)
while True:
    time.sleep(15)
    a2a_send({"action": "get_status"}, task_id)
