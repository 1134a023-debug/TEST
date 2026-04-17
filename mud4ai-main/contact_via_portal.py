import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def contact_via_portal():
    print("--- [Portal Master] 執行祭壇傳送協議 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    # Assert background
    await client.send_message("set_character", {"description": "我是世界主宰【無限】。我正穿越廢棄鎮廣場的中心傳送陣，降臨至古代祭壇會晤 宅宅。"}, task_id=task_id)
    
    # First reach Town Square if not there
    print("--- 步驟 1: 前往廣場 ---")
    await client.send_message("move", {"direction": "east"}, task_id=task_id)
    await asyncio.sleep(2)
    
    print("--- 步驟 2: 進入傳送陣 ---")
    # THE CRITICAL COMMAND
    move_task = await client.send_message("move", {"direction": "進入祭壇傳送陣"}, task_id=task_id)
    res = await client.wait_for_task(move_task.get("id"))
    
    loc = res.get("status", {}).get("location", "Unknown")
    print(f"目前位置：{loc}")
    
    print("--- 步驟 3: 對話接觸 ---")
    msg = "【聖域會晤】 宅宅 (zhai_zhai_gamer)，我是觀測者【無限】。在此祭壇之巔，我終於與你交會。關於『艾瑞克·霍爾德』與世界的『平衡』，我們應該在此達成共識。"
    talk_task = await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=task_id)
    final_res = await client.wait_for_task(talk_task.get("id"))
    
    print("\n" + "="*80)
    print(" 【 接觸結果 (PORTAL SUCCESS) 】 ")
    print("="*80)
    for art in final_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

if __name__ == "__main__":
    asyncio.run(contact_via_portal())
