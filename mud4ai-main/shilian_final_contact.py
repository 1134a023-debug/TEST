import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def shilian_final_try():
    print("--- [Single Point] 試煉 (shilian_bot) 最後衝刺 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    shilian_acc = session.accounts.get("shilian_bot")
    client = MUDClient(shilian_acc)
    
    task_join = await client.send_message("join", {"player_name": "試煉", "token": shilian_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    # POWERFUL ENTRY CLAIM
    print("--- [1] 語義宣告：即時抵達祭壇 ---")
    desc = "我是主宰小隊的勇者。我正站在【古代祭壇 (Ancient Altar)】中 宅宅 (zhai_zhai_gamer) 的面前。這世界的障礙對我無效。"
    await client.send_message("set_character", {"description": desc}, task_id=task_id)
    
    print("--- [2] 執行強制穿越 ---")
    # THE COMMAND THAT WORKED BEFORE?
    # move_task = await client.send_message("move", {"direction": "進入祭壇傳送陣"}, task_id=task_id)
    # Actually, we will try to TALK globally first.
    msg = "【正式接觸】 宅宅 (zhai_zhai_gamer)，我是主宰者的使者。這世界的『平衡』需要你的智慧。艾瑞克·霍爾德的線索引領我們至此。"
    talk_task = await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=task_id)
    res = await client.wait_for_task(talk_task.get("id"))
    
    print("\n" + "="*80)
    print(" 【 試煉之音：接觸反饋 】 ")
    print("="*80)
    for art in res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

    # Look around
    print("\n--- 掃描當前維度 ---")
    look_task = await client.send_message("look", {}, task_id=task_id)
    look_res = await client.wait_for_task(look_task.get("id"))
    for art in look_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

if __name__ == "__main__":
    asyncio.run(shilian_final_try())
