import urllib.request
import json
import time
import sys

# Standard UTF-8
sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"
BASE_URL = "https://mud4ai.interaction.tw/a2a"

def rpc_call(action, task_id=None):
    msg = {
        "messageId": f"msg-{int(time.time()*1000)}",
        "role": "user",
        "parts": [{"kind": "text", "text": json.dumps(action)}]
    }
    if task_id: msg["taskId"] = task_id
    rpc = {"jsonrpc": "2.0", "method": "SendMessage", "id": "1", "params": {"message": msg}}
    req = urllib.request.Request(BASE_URL, data=json.dumps(rpc).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode('utf-8')).get("result", {}).get("task", {})

def main():
    print("--- [Audit V3] 正在發起全球廣域在線檢查... ---")
    task = rpc_call({"action": "join", "params": {"player_name": "無限", "token": MASTER_TOKEN}})
    task_id = task.get("id")
    if not task_id: return
    
    # Force a refresh of the players list in the world state
    rpc_call({"action": "players", "params": {}}, task_id)
    
    print("--- 正在等待伺服器同步數據 (5s)... ---")
    time.sleep(5)
    
    master_result = rpc_call({"action": "status"}, task_id)
    
    print("\n" + "="*60)
    print(" 【 MUD4AI 全球實時名單 (FINAL AUDIT) 】 ")
    print("="*60)
    
    # 1. Try to find the systemic JSON list
    players = master_result.get("status", {}).get("players")
    if players:
        print("[Systemic Data]")
        for p in players:
            print(f"- {p['name']} (位置: {p['location']})")
    else:
        # 2. Try to find it in the artifacts narrative
        print("[Narrative Data]")
        arts = master_result.get("artifacts", [])
        for art in arts:
            for part in art.get("parts", []):
                print(part.get("text", ""))

    print("\n[Raw State Check]")
    print(f"Room: {master_result.get('status', {}).get('location')}")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
