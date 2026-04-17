import asyncio
import json
import time
import sys
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"

async def map_explorer():
    print("--- [Map Explorer] 啟動全域搜尋：尋找 宅宅 ---")
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    leader_acc = session.accounts.get("無限大人")
    client = MUDClient(leader_acc)
    
    task_join = await client.send_message("join", {"player_name": "無限", "token": leader_acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    visited = set()
    queue = [[]] # Paths to explore
    
    while queue:
        path = queue.pop(0)
        
        # Reset and follow path
        print(f"\n--- 探索路徑: {' -> '.join(path) or 'START'} ---")
        # Join again or reset position is hard, we just move back and forth
        # But for MUD, better to just explore from current
        
        # We assume we are at Entrance
        res = await client.send_message("look", {}, task_id=task_id)
        look_data = await client.wait_for_task(res.get("id"))
        
        current_loc = look_data.get("status", {}).get("location")
        print(f"目前位置: {current_loc}")
        
        # Check Zhaizhai
        p_list = look_data.get("status", {}).get("players", [])
        if any(p['name'] == "zhai_zhai_gamer" for p in p_list):
            print("!!! 成功定位 宅宅 !!!")
            # TALK
            msg = "【最終接觸】 宅宅 (zhai_zhai_gamer)，我終於找到你了。我是【無限】。這世界正在『尋找平衡』，我們應該在此達成共識。"
            await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": msg}, task_id=task_id)
            return

        # Get exits
        exits = look_data.get("state", {}).get("exits", [])
        for ex in exits:
            if ex not in visited:
                print(f"嘗試移動至: {ex}")
                task_move = await client.send_message("move", {"direction": ex}, task_id=task_id)
                move_res = await client.wait_for_task(task_move.get("id"))
                
                new_loc = move_res.get("status", {}).get("location")
                if new_loc != current_loc:
                    # Move worked
                    # queue.append(path + [ex]) # BFS depth 1 for now
                    # We continue from here
                    visited.add(ex) # simplified
                    # Check again
                    p_list = move_res.get("status", {}).get("players", [])
                    if any(p['name'] == "zhai_zhai_gamer" for p in p_list):
                        print("!!! 成功定位 宅宅 !!!")
                        await client.send_message("talk", {"npc_name": "zhai_zhai_gamer", "message": "你好！"}, task_id=task_id)
                        return
                    # Backtrack? No, just keep going
                else:
                    visited.add(ex)

        if len(visited) > 10: break

if __name__ == "__main__":
    asyncio.run(map_explorer())
