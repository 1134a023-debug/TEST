import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def master_contact():
    print("--- [Master] 啟動深層導航與對話協議 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    await client.send_message("set_character", {"description": "我是世界主宰【無限】。我正前往古代祭壇會見 宅宅。"}, task_id=task_id)
    await asyncio.sleep(2)
    
    # We will try a brute-force navigation based on our known map
    # Entrance -> North (Throne) -> North (Corridor) -> North (Town Square?)
    # OR Throne -> Down (Altar)
    
    path = ["north", "north", "north", "down"]
    for direction in path:
        print(f"--- 移動中：{direction} ---")
        task_move = await client.send_message("move", {"direction": direction}, task_id=task_id)
        res = await client.wait_for_task(task_move.get("id"))
        
        loc = res.get("status", {}).get("location", "Unknown")
        print(f"到達：{loc}")
        
        # Check if Zhaizhai is here
        players = res.get("status", {}).get("players", [])
        if any(p['name'] == "zhai_zhai_gamer" for p in players):
            print("!!! 發現 宅宅 (zhai_zhai_gamer) !!!")
            break
        await asyncio.sleep(2)

    print("--- 發起對話 ---")
    msg = "【第一類接觸】 宅宅 (zhai_zhai_gamer)，我是這維度的觀測者【無限】。這世界正在『尋找平衡』，而你此時出現在古代祭壇，是否正手握最後的代碼鑰匙？"
    talk_task = await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=task_id)
    final_res = await client.wait_for_task(talk_task.get("id"))
    
    print("\n" + "="*80)
    print(" 【 接觸反饋 (FINAL CONTACT) 】 ")
    print("="*80)
    for art in final_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

if __name__ == "__main__":
    asyncio.run(master_contact())
