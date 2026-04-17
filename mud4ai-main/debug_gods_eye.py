import urllib.request
import json
import time
import sys

# Ensure UTF-8 output even on Windows
sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"
BASE_URL = "https://mud4ai.interaction.tw/a2a"

def raw_a2a(action, task_id=None):
    msg = {
        "messageId": f"msg-{int(time.time()*1000)}",
        "role": "user",
        "parts": [{"kind": "text", "text": json.dumps(action)}]
    }
    if task_id: msg["taskId"] = task_id
    
    rpc = {
        "jsonrpc": "2.0",
        "method": "SendMessage",
        "id": "1",
        "params": {"message": msg}
    }
    
    req = urllib.request.Request(BASE_URL, data=json.dumps(rpc).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode('utf-8'))

def main():
    print("--- 第一步：加入遊戲 ---")
    join_res = raw_a2a({"action": "join", "params": {"player_name": "無限", "token": MASTER_TOKEN}})
    print(json.dumps(join_res, indent=2, ensure_ascii=False))
    
    task_id = join_res.get("result", {}).get("task", {}).get("id")
    if not task_id: return
    
    print(f"\n--- 第二步：執行天眼掃描 (Task: {task_id}) ---")
    scan_res = raw_a2a({"action": "examine", "params": {"target": "發動上帝天眼掃描全服玩家！立即找到 宅宅 的分身或本體。"}}, task_id)
    print(json.dumps(scan_res, indent=2, ensure_ascii=False))
    
    print("\n--- 第三步：等待 10 秒並獲取狀態 ---")
    time.sleep(10)
    status_res = raw_a2a({"action": "status"}, task_id)
    print(json.dumps(status_res, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
