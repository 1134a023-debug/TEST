import asyncio
import urllib.request
import json
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

# Mapping between tokens.json keys and character names
TOKEN_TO_NAME = {
    "無限大人": "無限",
    "heihe_bot": "黑河",
    "shilian_bot": "試煉",
    "molong_bot": "魔龍",
    "銀河": "銀河"
}

def load_tokens():
    with open("mud4ai-main/tokens.json", "r", encoding="utf-8") as f:
        return json.load(f)

def a2a_req(action, task_id=None):
    msg = {"messageId": f"msg-{int(time.time()*1000)}", "role": "user",
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
        res = urllib.request.urlopen(req, timeout=30)
        return json.loads(res.read().decode('utf-8')).get("result", {}).get("task", {})
    except Exception as e:
        print(f"Request error: {e}")
        return {}

async def a2a_send(action, task_id=None):
    return await asyncio.to_thread(a2a_req, action, task_id)

async def login_character(token_key, token_val):
    name = TOKEN_TO_NAME.get(token_key, token_key)
    print(f"[{name}] 正在上線...", flush=True)
    
    # Join the game
    task = await a2a_send({"action": "join", "params": {"player_name": name, "token": token_val}})
    task_id = task.get("id")
    
    if not task_id:
        print(f"[{name}] 上線失敗或連線逾時！", flush=True)
        return
    
    print(f"[{name}] 上線成功！(Task ID: {task_id})", flush=True)
    
    # Maintain session briefly and confirm status
    for i in range(2):
        await asyncio.sleep(5)
        status = await a2a_send({"action": "status"}, task_id)
        if "id" in status:
            print(f"[{name}] 狀態確認中... {i+1}", flush=True)
        else:
            print(f"[{name}] 連線可能已過期。", flush=True)
            break

async def main():
    try:
        tokens = load_tokens()
    except Exception as e:
        print(f"無法讀取 tokens.json: {e}")
        return

    print(f"=========================================")
    print(f"MUD4AI 全帳號集體上線程序啟動")
    print(f"找到 {len(tokens)} 個傳奇帳號，準備同步登入...")
    print(f"=========================================\n")
    
    tasks = [login_character(k, v) for k, v in tokens.items()]
    await asyncio.gather(*tasks)
    print("\n=========================================")
    print("所有帳號上線程序執行完畢。")
    print("=========================================")

if __name__ == "__main__":
    asyncio.run(main())
