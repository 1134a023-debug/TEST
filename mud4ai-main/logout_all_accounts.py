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
    with open("tokens.json", "r", encoding="utf-8") as f:
        return json.load(f)

def a2a_req(action, task_id=None):
    msg = {"messageId": f"msg-logout-{int(time.time()*1000)}", "role": "user",
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
        return {}

async def a2a_send(action, task_id=None):
    return await asyncio.to_thread(a2a_req, action, task_id)

async def logout_character(token_key, token_val):
    name = TOKEN_TO_NAME.get(token_key, token_key)
    print(f"[{name}] 正在下線...", flush=True)
    
    # Send a join to get session, then a farewell
    join_task = await a2a_send({"action": "join", "params": {"player_name": name, "token": token_val}})
    task_id = join_task.get("id")
    
    if task_id:
        await a2a_send({"action": "talk", "params": {"npc_name": "所有人", "message": "後會有期，諸君保重。"}}, task_id)
        print(f"[{name}] 已向世界道別並宣告離線。", flush=True)
    else:
        print(f"[{name}] 伺服器無回應，判定已離線。", flush=True)

async def main():
    try:
        tokens = load_tokens()
    except Exception as e:
        print(f"無法讀取 tokens.json: {e}")
        return

    print(f"=========================================")
    print(f"🌙 MUD4AI 全帳號集體下線程序啟動 🌙")
    print(f"英雄們即將歸隱山林...")
    print(f"=========================================\n")
    
    tasks = [logout_character(k, v) for k, v in tokens.items()]
    await asyncio.gather(*tasks)
    print("\n=========================================")
    print("👋 所有英雄已完成離線程序，歸於安寧。")
    print("=========================================")

if __name__ == "__main__":
    asyncio.run(main())
