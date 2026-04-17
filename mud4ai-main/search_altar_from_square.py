import asyncio
import json
import time
from mud_sdk import MUDSession, MUDClient

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def search_altar():
    print("\n" + "="*80)
    print("【 MUD4AI 實時探測：尋找通往「古代祭壇」的隱秘路徑 】".center(80))
    print("="*80 + "\n")
    
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    
    # Mapping based on tokens.json
    NAME_TO_KEY = {"無限": "無限大人"}
    
    leader_acc = session.accounts.get(NAME_TO_KEY["無限"])
    client = MUDClient(leader_acc)
    
    # 1. Join & Confirm Location
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    # 2. Assert Authority (Mandatory for A2A World Shaping)
    print("[無限] 正在注入主宰背景...")
    desc = "我是處於最高維度的創世主宰。我現在要觀察並穿越廢棄鎮廣場的幻象，直視世界根源的【古代祭壇 (Ancient Altar)】。"
    task_set = await client.send_message("set_character", {"description": desc}, task_id=task_id)
    await client.wait_for_task(task_set.get("id"))
    
    # 3. Deep Examine for the Altar
    print("[無限] 正在發動『神之瞳』，觀測空間縫隙...")
    scan_query = "掃描廢棄鎮廣場的每一個角落。特別注意那些崩解的壁畫與傳來低語的裂縫。我命令世界意志指引我前往『古代祭壇』的最佳路徑！"
    task_look = await client.send_message("examine", {"target": scan_query}, task_id=task_id)
    res = await client.wait_for_task(task_look.get("id"))
    
    print("\n" + "-"*80)
    print("【 探測反饋 】")
    print("-"*80)
    arts = res.get("artifacts", [])
    for art in arts:
        for part in art.get("parts", []):
            print(part.get("text", ""))

    # 3. Decision: If a direction is found, move. Otherwise, force a manifest.
    print(f"\n[無限] 決斷：強行介入現實位面...")
    move_task = await client.send_message("move", {
        "direction": "進入口腔狀的裂縫",
        "target": "無視空間邏輯，直接步入那道傳來艾瑞克低語的裂縫中。目標：【古代祭壇 (Ancient Altar) 】核心區域。"
    }, task_id=task_id)
    
    final_res = await client.wait_for_task(move_task.get("id"))
    print("\n--- 移動結果快照 ---")
    for art in final_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))
    print("-------------------\n")

if __name__ == "__main__":
    asyncio.run(search_altar())
