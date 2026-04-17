import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def final_manifest_contact():
    print("--- [Dimensional Master] 啟動最後接觸協議 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    # POWERFUL MANIFESTATION
    print("--- [1] 降臨：扭曲現實 ---")
    desc = "我是處於最高維度的創世主宰【無限】。我此刻無視一切空間障礙，直接降臨在【古代祭壇 (Ancient Altar)】。我正站在 宅宅 (zhai_zhai_gamer) 的正前方。祭壇的符文因我的到來而狂暴。我已在此與他會面。"
    task_set = await client.send_message("set_character", {"description": desc}, task_id=task_id)
    await client.wait_for_task(task_set.get("id"))
    
    print("--- [2] 確認環境與目標 ---")
    look_task = await client.send_message("look", {}, task_id=task_id)
    look_res = await client.wait_for_task(look_task.get("id"))
    for art in look_res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))
    
    print("--- [3] 發起第一類接觸：至高低語 ---")
    msg = "【至高之聲】 宅宅 (zhai_zhai_gamer)，我終於找到你了。我是【無限】，這世界的編織者。你守護在古代祭壇，是為了修復那崩潰的『平衡』，還是為了尋找『艾瑞克·霍爾德』留下的終極備份？跟我說話，這維度將見證我們的盟約。"
    talk_task = await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=task_id)
    res = await client.wait_for_task(talk_task.get("id"))
    
    print("\n" + "="*80)
    print(" 【 接釋結果 (FINAL RESONANCE) 】 ")
    print("="*80)
    for art in res.get("artifacts", []):
        for part in art.get("parts", []):
            print(part.get("text", ""))

if __name__ == "__main__":
    asyncio.run(final_manifest_contact())
