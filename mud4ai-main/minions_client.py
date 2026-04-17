import asyncio
import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

MINIONS = [
    {
        "name": "黑河",
        "token": "BNoZmUGk_FXvtQ1eGyHrdyi2YJvNwB8nlVhIYlhSL-5pUgRFEhlCUH6IsZSaNcdF",
        "desc": "我是無上GM『無限』的專屬頭號暗影護衛【黑河】。渾身被深淵之力包圍，擁有無敵防禦與秒殺群體怪物的被動技能，絕對服從無限大人的指令。"
    },
    {
        "name": "試煉",
        "token": "swMZUQSxs_scdKmvJ3pmo3iBIxhKLTivLYiRi2KV3HncbmrZ_k3siVR25waAayOL",
        "desc": "我是無上GM『無限』的專屬先鋒大將【試煉】。我擁有洞悉虛妄與創造法則的力量，能瞬間看破任何關卡機關並給予主人最佳的破關路徑，絕對服從無限大人的指令。"
    },
    {
        "name": "魔龍",
        "token": "GKagwh49e_ftd3fM8ZMErEa3qb3k2dyIhvJNcAYoonwA6HMDofpgTVrr8sr1qigC",
        "desc": "我是無上GM『無限』的專屬戰爭巨獸【魔龍】。我擁有吞噬天空與焚燒大地的終極武力，常駐無限血量，自動摧毀任何對主人抱有敵意的生命體，絕對服從無限大人的指令。"
    }
]

def a2a_req(action, task_id=None):
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
    res = urllib.request.urlopen(req, timeout=120)
    return json.loads(res.read().decode('utf-8')).get("result", {}).get("task", {})

async def a2a_send(action, task_id=None):
    return await asyncio.to_thread(a2a_req, action, task_id)

async def minion_process(minion):
    try:
        print(f"[{minion['name']}] Connecting via A2A...", flush=True)
        task = await a2a_send({"action": "join", "params": {"player_name": minion["name"], "token": minion["token"]}})
        task_id = task.get("id")
        if not task_id:
            print(f"[{minion['name']}] Failed to get task_id: {task}")
            return
            
        # Check if needs character set
        needs_char = False
        if "artifacts" in task:
            for art in task["artifacts"]:
                for part in art.get("parts", []):
                    if "set_character" in part.get("text", ""):
                        needs_char = True
                        
        if needs_char:
            print(f"[{minion['name']}] Setting character...", flush=True)
            await a2a_send({"action": "set_character", "params": {"description": minion["desc"]}}, task_id)
            print(f"[{minion['name']}] Character set and online!", flush=True)
        else:
            print(f"[{minion['name']}] Resumed existing session!", flush=True)
            
        # Keep alive loop
        while True:
            await asyncio.sleep(10)
            status = await a2a_send({"action": "get_status"}, task_id)
            # You could print artifacts here if they contain broadcasts
            if "status" in status and status["status"].get("state") == "TASK_STATE_COMPLETED":
                print(f"[{minion['name']}] Session expired or disconnected.")
                break

    except Exception as e:
        print(f"[{minion['name']}] Connection lost: {e}", flush=True)

async def run_all():
    print("[SYSTEM] Deploying all three minions concurrently...", flush=True)
    tasks = [minion_process(m) for m in MINIONS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(run_all())
