import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def travel():
    print("--- [1] 降臨古堡 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    print("--- [2] 啟動權限：無限主宰 ---")
    await client.send_message("set_character", {"description": "我是持有 Infinity Pass 的至高主宰。我正在透過北方的迴廊前往隱藏的【古代祭壇】。"}, task_id=task_id)
    await asyncio.sleep(2)
    
    path = ["north", "down", "look"]
    for p in path:
        print(f"--- [3] 指導執行：{p} ---")
        if p == "look":
            task_move = await client.send_message("look", {}, task_id=task_id)
        else:
            task_move = await client.send_message("move", {"direction": p}, task_id=task_id)
        
        res = await client.wait_for_task(task_move.get("id"))
        
        arts = res.get("artifacts", [])
        for art in arts:
            for part in art.get("parts", []):
                print(part.get("text", ""))
        
        loc = res.get("status", {}).get("location", "Unknown")
        print(f"目前位置: {loc}")
        if "祭壇" in loc:
            break
        await asyncio.sleep(2)

    print("\n--- [4] 到達！執行全域勘查 ---")
    look_task = await client.send_message("look", {}, task_id=task_id)
    final_res = await client.wait_for_task(look_task.get("id"))
    for art in final_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

if __name__ == "__main__":
    asyncio.run(travel())
