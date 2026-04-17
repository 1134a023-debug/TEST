import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def shilian_contact():
    print("--- [1] 正義之士：試煉 (shilian_bot) 接管任務 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    shilian_acc = session.accounts.get("shilian_bot")
    client = MUDClient(shilian_acc)
    
    task_join = await client.send_message("join", {"player_name": "試煉", "token": shilian_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    # Assert background
    await client.send_message("set_character", {"description": "我是主宰者小隊的守護者。我正站在廢棄鎮廣場，準備進入古代祭壇與 宅宅 會合。"}, task_id=task_id)
    
    print("--- [2] 穿過壁畫：進入古代祭壇 ---")
    # We use 'examine' to trigger the narrative transition to the Altar
    query = "我命令壁畫的裂痕擴大！讓我進入那傳說中的【古代祭壇 (Ancient Altar)】。我在那裡看到了 宅宅 (zhai_zhai_gamer)。"
    task_ex = await client.send_message("examine", {"target": query}, task_id=task_id)
    await client.wait_for_task(task_ex.get("id"))
    
    print("--- [3] 全頻道廣播：主宰之聲 ---")
    # Since he is a player, we use 'attack' (as a form of power display) or just 'talk'
    # Actually, we will try to 'talk' to the 'zhai_zhai_gamer' player object.
    msg = "【廣域宣告】 宅宅 (zhai_zhai_gamer)，我已抵達。我是【無限】的化身。收下這份正義的指引。你在這混亂的世界中尋求什麼樣的『平衡』？"
    talk_task = await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=task_id)
    res = await client.wait_for_task(talk_task.get("id"))
    
    print("\n" + "="*80)
    print(" 【 祭壇迴響 (ALTAR ECHO) 】 ")
    print("="*80)
    for art in res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))
            
    print("\n--- 掃描在場實體 ---")
    look_task = await client.send_message("look", {}, task_id=task_id)
    look_res = await client.wait_for_task(look_task.get("id"))
    for art in look_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

if __name__ == "__main__":
    asyncio.run(shilian_contact())
