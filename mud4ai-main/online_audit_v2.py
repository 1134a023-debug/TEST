import urllib.request
import json
import time
import sys

# Standard UTF-8
sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"
BASE_URL = "https://mud4ai.interaction.tw/a2a"

def final_audit():
    print("--- [Audit] 正在發送實時查詢請求... ---")
    msg = {
        "messageId": f"msg-audit-{int(time.time()*1000)}",
        "role": "user",
        "parts": [{"kind": "text", "text": json.dumps({"action": "players", "params": {}})}]
    }
    rpc = {
        "jsonrpc": "2.0", "method": "SendMessage", "id": "audit", "params": {"message": msg}
    }
    
    req = urllib.request.Request(BASE_URL, data=json.dumps(rpc).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as res:
        resp = json.loads(res.read().decode('utf-8'))
        task = resp.get("result", {}).get("task", {})
        task_id = task.get("id")
        
        # Poll briefly for the players state updates in the task result
        for i in range(5):
            time.sleep(2)
            rpc_status = {
                "jsonrpc": "2.0", "method": "SendMessage", "id": "status",
                "params": {"message": {"messageId": f"msg-s-{i}", "role": "user", "parts": [{"kind": "text", "text": json.dumps({"action": "status"})}], "taskId": task_id}}
            }
            req_s = urllib.request.Request(BASE_URL, data=json.dumps(rpc_status).encode('utf-8'), headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req_s) as res_s:
                s_resp = json.loads(res_s.read().decode('utf-8'))
                state_obj = s_resp.get("result", {}).get("task", {}).get("status", {})
                players = state_obj.get("players")
                if players:
                    print("\n" + "="*50)
                    print(" 【 MUD4AI 實時在線名單 (V2) 】 ")
                    print("="*50)
                    for p in players:
                        print(f"- {p['name']} (位置: {p['location']})")
                    print("="*50 + "\n")
                    return

    print("未能獲取結構化列表。請檢視原始任務狀態。")

if __name__ == "__main__":
    final_audit()
