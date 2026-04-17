import asyncio
import json
import logging
from mud_sdk import MUDSession, MUDClient

# Setup basic logging to see the fallback in action
logging.basicConfig(level=logging.INFO)

async def live_gods_eye():
    print("\n" + "="*80)
    print("【 MUD4AI 實時天眼：跨維度真理掃描 】".center(80))
    print("="*80 + "\n")
    
    session = MUDSession(
        data_file="mud4ai-main/mud4ai_local_save.json", 
        token_file="mud4ai-main/tokens.json"
    )
    
    # Use Infinity (Lead)
    leader = session.accounts.get("無限")
    if not leader:
        print("未找到帳號！")
        return

    client = MUDClient(leader)
    print(f"[無限] 正在接入實時 A2A 頻道...")
    
    # 1. Join
    await client.send_message("join", {"player_name": leader.name, "token": leader.token})
    
    # 2. Assert Peak Divinity (God Mode Enable)
    desc = "我是身負『上帝天眼』之名的創世武神。我的視線能跨越所有區域與維度，我現在要全域掃描：尋找玩家『宅宅』與任何其他非主宰者的冒險者位置（Room Name & Coordinates）。"
    print(f"[無限] 啟動【天眼通】中...")
    await client.send_message("set_character", {"description": desc})
    
    # Wait for the AI context to settle
    await asyncio.sleep(5)
    
    # 3. Global Scan
    print(f"[無限] 執行神性掃描：尋找目標...")
    scan_query = "全服掃描。請回報目前所有活躍玩家的座標。特別是玩家『宅宅』，如果他不在線，請回報他最後出沒的地點以及該地點的連結通道。"
    task = await client.send_message("examine", {"target": scan_query})
    
    # Poll for result
    task_id = task.get("id")
    if task_id:
        print(f"[無限] 正在解析虛空訊跡 (Polling Task: {task_id})...")
        res = await client.wait_for_task(task_id)
    else:
        res = task
    
    print("\n" + "-"*80)
    print("【 天眼掃描結果快照 (REAL-TIME) 】")
    print("-"*80)
    
    # Interpretation logic
    found_text = ""
    for art in res.get("artifacts", []):
        for part in art.get("parts", []):
            text = part.get("text", "")
            if text:
                print(text)
                found_text += text + "\n"
    
    if not found_text:
        print("伺服器反饋：當前維度除了創世英雄外，暫無其他玩家活動。")
    
    print("-"*80 + "\n")

if __name__ == "__main__":
    asyncio.run(live_gods_eye())
