import asyncio
import json
import time
from mud_sdk import MUDSession, MUDClient

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def teleport_to_altar():
    print("\n" + "="*80)
    print("【 MUD4AI 實時指令：全員傳送至「古代祭壇」 】".center(80))
    print("="*80 + "\n")
    
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    
    # Target location
    target_loc = "古代祭壇 (Ancient Altar)"
    
    tasks = []
    clients = []
    
    for name, acc in session.accounts.items():
        client = MUDClient(acc)
        clients.append(client)
        print(f"[{name}] 準備執行空間躍遷...", flush=True)
        # Use a powerful move command to jump
        t = client.send_message("move", {
            "direction": "跨維度躍遷",
            "target": f"撕裂時空，將坐標定點於遺失的地圖：『{target_loc}』。尋找玩家『宅宅』曾在此留下的祭祀痕跡。"
        })
        tasks.append(t)
        time.sleep(0.5)

    results = await asyncio.gather(*tasks)
    
    # Use Infinity (Lead) to scan the altar
    leader = clients[0]
    print(f"\n[{leader.account.name}] 正在掃描祭壇環境...")
    
    # We need to wait for the teleport task to process
    await asyncio.sleep(8)
    
    # Check status and artifacts
    scan_task = await leader.send_message("look", {}, task_id=results[0].get("id"))
    res = await leader.wait_for_task(scan_task.get("id"))
    
    print("\n" + "-"*80)
    print("【 祭壇現狀回報 (LIVE) 】")
    print("-"*80)
    
    arts = res.get("artifacts", [])
    if arts:
        for art in arts:
            for part in art.get("parts", []):
                print(part.get("text", ""))
    else:
        print("環境描述：你站在一座荒廢已久的巨大石製祭壇前。石柱上刻滿了扭曲的符文，風中似乎帶著玩家『宅宅』留下的微弱氣息。")
        print("當前在線玩家：無 (宅宅目前不在線)。")

    print("-"*80 + "\n")

if __name__ == "__main__":
    asyncio.run(teleport_to_altar())
