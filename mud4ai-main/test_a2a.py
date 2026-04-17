import urllib.request, json

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
    try:
        res = urllib.request.urlopen(req, timeout=10)
        return json.loads(res.read().decode()).get("result", {}).get("task", {})
    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}

print("Attempting to join with token...")
task = a2a_send({"action": "join", "params": {
    "player_name": "黑河", 
    "token": "BNoZmUGk_FXvtQ1eGyHrdyi2YJvNwB8nlVhIYlhSL-5pUgRFEhlCUH6IsZSaNcdF"
}})
print("Join Task:", json.dumps(task, indent=2, ensure_ascii=False))

if "id" in task:
    task_id = task["id"]
    print(f"\nGot task_id: {task_id}. Attempting to get_status...")
    status_task = a2a_send({"action": "get_status"}, task_id=task_id)
    
    if "messages" in status_task and len(status_task["messages"]) > 0:
        last_msg = status_task["messages"][-1]
        if "parts" in last_msg and len(last_msg["parts"]) > 0:
            print("Status Output:", last_msg["parts"][-1].get("text", ""))
    else:
        print("Full status response:", json.dumps(status_task, indent=2, ensure_ascii=False))
        
    a2a_send({"action": "leave"}, task_id=task_id)
