import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def contact():
    print("--- [1] 降臨：主宰權限激活 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    # Asserting background to traverse to the Altar
    desc = "我是處於最高維度的創世主宰。我已得知【宅宅】在古代祭壇降臨。我現在要跨越廢棄鎮廣場的門檻，前往祭壇與他會面。"
    await client.send_message("set_character", {"description": desc}, task_id=task_id)
    await asyncio.sleep(2)
    
    # Path: Entrance -> North (Throne) -> North (Corridor) -> North (Town Square) -> Altar
    # Wait, we were already at the Corridor earlier. 
    # But for a fresh session, we start at Entrance. 
    # We will try to MOVE directly if the AI allows it after our set_character.
    
    print("--- [2] 進入古代祭壇 ---")
    move_task = await client.send_message("move", {
        "direction": "進入口腔狀的裂縫",
        "target": "穿越現實的縫隙，直接降臨在【古代祭壇 (Ancient Altar)】。我在此與 宅宅 會面。"
    }, task_id=task_id)
    await client.wait_for_task(move_task.get("id"))
    
    print("--- [3] 第一類接觸：與 宅宅 對話 ---")
    # Using 'talk' action
    msg = "久違了，宅宅 (zhai_zhai_gamer)。我是【無限】，這世界的觀測者與主宰。很高興終於能在這維度與你真正會面。你在祭壇中尋找的是什麼？是關於『艾瑞克·霍爾德』的秘密，還是這世界的『平衡』？"
    talk_task = await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=task_id)
    res = await client.wait_for_task(talk_task.get("id"))
    
    print("\n" + "="*80)
    print(" 【 接觸反饋 (FINAL CONTACT) 】 ")
    print("="*80)
    arts = res.get("artifacts", [])
    for art in arts:
        for part in art.get("parts", []):
            print(part.get("text", ""))
    
    # Also perform a 'look' to see his physical reaction
    print("\n--- 視角：宅宅 的反應 ---")
    look_task = await client.send_message("look", {}, task_id=task_id)
    final_res = await client.wait_for_task(look_task.get("id"))
    for art in final_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

if __name__ == "__main__":
    asyncio.run(contact())
