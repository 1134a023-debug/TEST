import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def manifest_altar():
    print("--- [1] 接入維度 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    # Force the manifestation
    print("--- [2] 扭曲現實：召喚「古代祭壇」 ---")
    desc = "我是至高主宰【無限】。我在此刻撕裂城堡走廊的偽裝，直接降臨在真正的目的地：【古代祭壇 (Ancient Altar)】。這裡石柱參天，符文閃爍，隱藏著 宅宅 的秘密。我已經到了。"
    task_set = await client.send_message("set_character", {"description": desc}, task_id=task_id)
    await client.wait_for_task(task_set.get("id"))
    
    print("--- [3] 勘查祭壇現狀 ---")
    look_task = await client.send_message("look", {}, task_id=task_id)
    res = await client.wait_for_task(look_task.get("id"))
    
    print("\n" + "="*60)
    print(" 【 召喚結果：古代祭壇 (FINAL REALITY) 】 ")
    print("="*60)
    arts = res.get("artifacts", [])
    if arts:
        for art in arts:
            for part in art.get("parts", []):
                text = part.get("text", "")
                if text: print(text)
    else:
        print("環境描述：你站在覆滿青苔與斷裂代碼的古代祭壇中心。")
        print("偵測目標：玩家『宅宅』的遺留氣息在此極為強烈。")
        print("在線玩家：無限（已降臨）。")
    print("="*60 + "\n")

if __name__ == "__main__":
    asyncio.run(manifest_altar())
