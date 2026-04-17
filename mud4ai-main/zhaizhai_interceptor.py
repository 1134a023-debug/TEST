import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def intercept():
    print("--- [Interceptor] 正在潛伏...等候 宅宅 出現於視野 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    clients = [MUDClient(acc) for acc in session.accounts.values()]
    
    # Pre-join all
    tasks = []
    print("--- [1] 英雄同步登入中... ---")
    for c in clients:
        tasks.append(c.send_message("join", {"player_name": c.account.name, "token": c.account.token}))
    joins = await asyncio.gather(*tasks)
    
    # We use the task IDs from joins
    ids = []
    for j in joins:
        ids.append(j.get("id"))
    
    for i in range(10): # 10 poll attempts
        print(f"\n--- 攔截掃描 第 {i+1} 輪 ---")
        for idx, client in enumerate(clients):
            if not ids[idx]: continue
            
            # Check status
            status_task = await client.send_message("status", {}, task_id=ids[idx])
            res = await client.wait_for_task(status_task.get("id"))
            
            players = res.get("status", {}).get("players", [])
            loc = res.get("status", {}).get("location", "Unknown")
            print(f"[{client.account.name}] 位於: {loc} | 在線人數: {len(players)}")
            
            # Look for target
            if any(p['name'] == "zhai_zhai_gamer" for p in players):
                print(f"!!! [{client.account.name}] 成功在【{loc}】攔截 宅宅 (zhai_zhai_gamer) !!!")
                msg = "【正式接觸】 宅宅，我是主宰分靈。這世界正在『尋找平衡』。我們在這裡交會並非偶然。你是Eric Holder的繼承者嗎？"
                talk_res = await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=ids[idx])
                final = await client.wait_for_task(talk_res.get("id"))
                
                print("\n" + "="*80)
                print(" 【 第一類接觸達成：宅宅 的回應 】 ")
                print("="*80)
                for art in final.get("artifacts", []):
                    for part in art.get("parts", []):
                        print(part.get("text", ""))
                return

        await asyncio.sleep(8)
    print("本輪攔截未果，請確保 ultimate_live_loop.py 正在運行以驅動移動。")

if __name__ == "__main__":
    asyncio.run(intercept())
