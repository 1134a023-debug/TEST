import asyncio
import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"

def a2a_req(action, task_id=None, timeout=60):
    msg = {"messageId": f"msg-{int(time.time()*1000)}", "role": "user",
           "parts": [{"kind": "text", "text": json.dumps(action)}]}
    if task_id:
        msg["taskId"] = task_id
    req = urllib.request.Request(
        "https://mud4ai.interaction.tw/a2a",
        data=json.dumps({"jsonrpc": "2.0", "method": "SendMessage", "id": "1", "params": {"message": msg}}).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        res = urllib.request.urlopen(req, timeout=timeout)
        return json.loads(res.read().decode('utf-8')).get("result", {}).get("task", {})
    except Exception as e:
        print(f"Request error: {e}")
        return {}

async def main():
    print("正在以 [無限] 身分調取伺服器底層玩家清單...")
    
    # 1. Join
    task = a2a_req({"action": "join", "params": {"player_name": "無限", "token": MASTER_TOKEN}})
    task_id = task.get("id")
    if not task_id: return

    # 2. Systemic Players Command
    print("[系統] 執行 action: players ...")
    t_res = a2a_req({"action": "players", "params": {}}, task_id=task_id)
    
    # Also check if there's any world chat or broadcast in the history
    print("[系統] 執行 action: look (檢查當前房間有無其他玩家跡象)...")
    t_look = a2a_req({"action": "look", "params": {}}, task_id=task_id)
    
    print("\n--- 🔍 系統反饋清單 ---")
    
    # Extract any list of players from the task state or artifacts
    # Since artifact text might be narrative, we look at the raw state if possible via print
    for art in t_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

    print("\n--- 📍 當前位置玩家見聞 ---")
    for art in t_look.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))
    
if __name__ == "__main__":
    asyncio.run(main())
