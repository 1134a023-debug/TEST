import urllib.request
import json
import time
import sys

# Standard UTF-8
sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"
BASE_URL = "https://mud4ai.interaction.tw/a2a"

def simple_a2a_check():
    print("--- [1] 加入遊戲 (普通模式) ---")
    msg_join = {
        "messageId": f"msg-join-{int(time.time()*1000)}",
        "role": "user",
        "parts": [{"kind": "text", "text": json.dumps({"action": "join", "params": {"player_name": "無限", "token": MASTER_TOKEN}})}]
    }
    
    rpc_join = {
        "jsonrpc": "2.0", "method": "SendMessage", "id": "join",
        "params": {"message": msg_join}
    }
    
    req_join = urllib.request.Request(BASE_URL, data=json.dumps(rpc_join).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req_join) as res:
        task = json.loads(res.read().decode('utf-8')).get("result", {}).get("task", {})
        task_id = task.get("id")
    
    if not task_id:
        print("無法取得連線 ID")
        return

    print(f"--- [2] 查詢在線玩家 (Task: {task_id}) ---")
    # Using the standard systemic 'players' action
    msg_players = {
        "messageId": f"msg-players-{int(time.time()*1000)}",
        "role": "user",
        "parts": [{"kind": "text", "text": json.dumps({"action": "players", "params": {}})}],
        "taskId": task_id
    }
    
    rpc_players = {
        "jsonrpc": "2.0", "method": "SendMessage", "id": "players",
        "params": {"message": msg_players}
    }
    
    req_players = urllib.request.Request(BASE_URL, data=json.dumps(rpc_players).encode('utf-8'), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req_players) as res:
        result = json.loads(res.read().decode('utf-8'))
        # Immediate state check
        print("\n--- 📍 伺服器即時玩家數據 ---")
        state = result.get("result", {}).get("task", {}).get("status", {}).get("state")
        print(f"Server Task State: {state}")
        
        # Look for the players list in the result artifacts or state changes if it exists
        # In this SDK, we usually get it from the 'players' command feedback in narrative or raw keys
        
        # We also wait a few seconds and check status again to be 100% sure
        time.sleep(5)
        msg_status = {
            "messageId": f"msg-status-{int(time.time()*1000)}",
            "role": "user",
            "parts": [{"kind": "text", "text": json.dumps({"action": "status"})}, {"kind": "text", "text": "請直接列出目前在線的所有玩家名字，不要帶任何劇情。"}],
            "taskId": task_id
        }
        rpc_status = {
            "jsonrpc": "2.0", "method": "SendMessage", "id": "status",
            "params": {"message": msg_status}
        }
        req_status = urllib.request.Request(BASE_URL, data=json.dumps(rpc_status).encode('utf-8'), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req_status) as res:
            final_res = json.loads(res.read().decode('utf-8'))
            print("\n--- 📊 最終系統判定名單 ---")
            # Print the actual text response from the AI which should contain the player list
            arts = final_res.get("result", {}).get("task", {}).get("artifacts", [])
            for art in arts:
                for part in art.get("parts", []):
                    print(part.get("text", ""))

if __name__ == "__main__":
    simple_a2a_check()
