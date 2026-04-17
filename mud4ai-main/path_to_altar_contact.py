import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def path_contact():
    print("--- [Path Master] 執行東線轉進協議 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    await client.send_message("set_character", {"description": "我是主宰【無限】。我正穿越廢棄鎮廣場，降臨至古代祭壇會晤 宅宅。"}, task_id=task_id)
    
    # Path: Entrance -> East (Town Square) -> Altar
    # We will try 'east' then 'enter' or 'down'
    
    path = ["east", "down", "look"]
    for direction in path:
        print(f"--- 移動中：{direction} ---")
        if direction == "look":
            task_move = await client.send_message("look", {}, task_id=task_id)
        else:
            task_move = await client.send_message("move", {"direction": direction}, task_id=task_id)
        res = await client.wait_for_task(task_move.get("id"))
        
        loc = res.get("status", {}).get("location", "Unknown")
        print(f"到達：{loc}")
        
    print("--- 最終嘗試對話 ---")
    msg = "【正式接觸】 宅宅 (zhai_zhai_gamer)，我是【無限】。世界意志指引我在此與你會合。關於『艾瑞克·霍爾德』的秘密，你是否已有定論？我們可以共同達成世界的『平衡』。"
    talk_task = await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=task_id)
    final_res = await client.wait_for_task(talk_task.get("id"))
    
    print("\n" + "="*80)
    print(" 【 接觸反饋 (PATH FINAL) 】 ")
    print("="*80)
    for art in final_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

if __name__ == "__main__":
    asyncio.run(path_contact())
