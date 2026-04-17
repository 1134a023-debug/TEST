import json, urllib.request, time

# Load tokens
with open('tokens.json', 'r', encoding='utf-8') as f:
    tokens = json.load(f)

# Characters to act (use keys from tokens.json)
characters = [
    {"name": name, "token": token}
    for name, token in tokens.items()
]

def a2a_req(action, task_id=None):
    msg = {
        "messageId": f"msg-{int(time.time()*1000)}",
        "role": "user",
        "parts": [{"kind": "text", "text": json.dumps(action)}]
    }
    if task_id:
        msg["taskId"] = task_id
    req = urllib.request.Request(
        "https://mud4ai.interaction.tw/a2a",
        data=json.dumps({
            "jsonrpc": "2.0",
            "method": "SendMessage",
            "id": "1",
            "params": {"message": msg}
        }).encode('utf-8'),
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            parsed = json.loads(res.read().decode('utf-8'))
            return parsed.get("result", {}).get("task", {})
    except Exception as e:
        print(f"Request error: {e}")
        return {}

def join_and_quest(char):
    name = char["name"]
    token = char["token"]
    print(f"[{name}] Joining game...")
    join_task = a2a_req({"action": "join", "params": {"player_name": name, "token": token}})
    task_id = join_task.get("id")
    if not task_id:
        print(f"[{name}] Join failed.")
        return
    # After joining, request quest list (or specific quest)
    print(f"[{name}] Requesting quest list...")
    quest_task = a2a_req({"action": "quest"}, task_id)
    # Simple output
    print(f"[{name}] Quest response: {quest_task}\n")

for ch in characters:
    join_and_quest(ch)
