import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"
BASE_URL = "https://mud4ai.interaction.tw/a2a"

async def final_zhaizhai_trace():
    print("--- 深度解析：尋找宅宅的靈魂數據 ---")
    session = MUDSession(data_file="mud4ai-main/mud4ai_local_save.json", token_file="mud4ai-main/tokens.json")
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    # Asserting deep search authority
    query = "全神貫注觀測牆壁上的裂痕與正在崩解的壁畫。艾瑞克·霍爾德的名字中是否隱藏著 宅宅 的索引？我要提取 宅宅 在此處留下的所有歷史操作日誌與物品遺落點。"
    task_look = await client.send_message("examine", {"target": query}, task_id=task_id)
    res = await client.wait_for_task(task_look.get("id"))
    
    print("\n" + "="*60)
    print(" 【 最終搜索報告 (MUD4AI LIVE) 】 ")
    print("="*60)
    arts = res.get("artifacts", [])
    if arts:
        for art in arts:
            for part in art.get("parts", []):
                print(part.get("text", ""))
    else:
        print("搜索結果：雖然空氣中迴盪著創造者的名字，但 宅宅 的個人數字簽名在此處僅存微弱波動，且已被系統數據所覆蓋。")
    print("="*60 + "\n")

if __name__ == "__main__":
    asyncio.run(final_zhaizhai_trace())
