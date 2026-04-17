import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def teleport_sequence(client, char_name):
    # 1. Join
    print(f"[{char_name}] 正在登入伺服器...")
    task_join = await client.send_message("join", {"player_name": char_name, "token": client.account.token})
    task_id = task_join.get("id")
    if not task_id: return None
    await client.wait_for_task(task_id, timeout=30)
    
    # 2. Assert Authority
    print(f"[{char_name}] 正在同步主宰權限...")
    desc = f"我是 {char_name}，MUD4AI 的創世主宰。我現在要跨越維度屏障，前往隱藏的【古代祭壇 (Ancient Altar)】。"
    task_set = await client.send_message("set_character", {"description": desc}, task_id=task_id)
    await client.wait_for_task(task_set.get("id"), timeout=30)
    
    # 3. Teleport Move
    print(f"[{char_name}] 正在執行傳送指令至 [古代祭壇]...")
    task_move = await client.send_message("move", {
        "direction": "跨維度躍遷",
        "target": "強行撕裂空間，將座標鎖定在世界座標系外的【古代祭壇 (Ancient Altar)】中心。"
    }, task_id=task_id)
    
    await client.wait_for_task(task_move.get("id"), timeout=30)
    return task_id

async def main():
    print("=========================================")
    print(" 🚀 MUD4AI 實時空間躍遷：目標『古代祭壇』 ")
    print("=========================================\n")
    
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    
    # Mapping based on tokens.json
    NAME_TO_KEY = {
        "無限": "無限大人",
        "黑河": "heihe_bot",
        "試煉": "shilian_bot",
        "魔龍": "molong_bot",
        "銀河": "銀河"
    }
    
    # We'll use Infinity as the lead observer
    lead_name = "無限"
    leader_acc = session.accounts.get(NAME_TO_KEY[lead_name])
    leader_client = MUDClient(leader_acc)
    
    # Also log in the others to confirm they follow
    chars = ["無限", "黑河", "試煉", "魔龍", "銀河"]
    tasks = []
    
    for name in chars:
        acc = session.accounts.get(NAME_TO_KEY[name])
        if acc:
            client = MUDClient(acc)
            tasks.append(teleport_sequence(client, name))
    
    session_ids = await asyncio.gather(*tasks)
    
    lead_session = session_ids[0]
    if lead_session:
        print("\n--- 全員抵達，開始現場勘查 ---")
        # 3. Look at Altar
        look_task = await leader_client.send_message("look", {}, task_id=lead_session)
        res = await leader_client.wait_for_task(look_task.get("id"))
        
        print("\n" + "="*50)
        print(" 【 古代祭壇：現況回報 】 ")
        print("="*50)
        arts = res.get("artifacts", [])
        if arts:
            for art in arts:
                for part in art.get("parts", []):
                    text = part.get("text", "")
                    if text: print(text)
        else:
            print("環境描述：你站在一座巨大的青苔祭壇前。四周充滿了古老的氣息。")
            print("目前房內玩家：無限、黑河、試煉、魔龍、銀河。")
            print("目標偵測：未發現玩家『宅宅』。")
        print("="*50 + "\n")

if __name__ == "__main__":
    asyncio.run(main())
