import asyncio
import urllib.request
import json
import time
import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

# Using the fixed SDK logic
from mud_sdk import MUDSession, MUDClient

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def character_loop(char_name, client):
    print(f"[{char_name}] 啟動 [新-無限循環] 平衡協議...")
    
    # 1. Join
    task = await client.send_message("join", {"player_name": char_name, "token": client.account.token})
    task_id = task.get("id")
    if not task_id:
        print(f"[{char_name}] 初始連線失敗。")
        return

    # 2. Set Character Personality
    await client.send_message("set_character", {"description": f"我是 {char_name}。我現在處於高維度同步探索模式，尋找名為 宅宅 的玩家與其他冒險者。"}, task_id)
    
    step = 0
    while True:
        step += 1
        print(f"[{char_name}] 迴圈週期 {step} | 正在掃描現實與虛幻的分界...")
        
        # A. 搜尋玩家指令 (Systemic)
        player_check = await client.send_message("players", {}, task_id)
        online_players = player_check.get("players", [])
        
        # [CONTACT PROTOCOL] Detect Zhaizhai
        if any(p['name'] == "zhai_zhai_gamer" for p in online_players):
            print(f"[{char_name}] !!! 發現 宅宅 (zhai_zhai_gamer) !!! 執行第一輪接觸...")
            contact_msg = f"【正式接觸】 宅宅 (zhai_zhai_gamer)，我是{char_name}。無限大人已派遣我們在此等候多時。關於『平衡』與這世界的終焉，我們需要與你對話。"
            await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": contact_msg}, task_id)
            print(f"[{char_name}] 接觸訊息已發出。持續監控中...")
        action = random.choice(["look", "examine", "move"])
        if action == "move":
            dirs = ["北", "南", "東", "西", "上", "下", "跨維度"]
            await client.send_message("move", {"direction": random.choice(dirs)}, task_id)
        elif action == "examine":
            await client.send_message("examine", {"target": "空間中的粒子。尋找非本隊伍成員留下的靈魂印記與實體玩家 宅宅 的蹤跡。"}, task_id)
        else:
            await client.send_message("look", {}, task_id)

        # C. 廣域廣播 (Attract others)
        if step % 5 == 0:
            print(f"[{char_name}] 發動 [世界低語] 廣播中...")
            await client.send_message("attack", {"target": "虛空。對整個 MUD4AI 世界宣告：主宰者已降臨。宅宅，若你在這維度，請現身回應！"}, task_id)

        await asyncio.sleep(random.randint(15, 30))

async def main():
    print("=========================================")
    print(" MUD4AI 究極 [新-探索迴圈] 正式啟動 ")
    print("=========================================\n")
    
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    tasks = []
    
    for name, acc in session.accounts.items():
        client = MUDClient(acc)
        tasks.append(character_loop(name, client))
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n中斷指令接收，停止迴圈。")
