import asyncio
import json
import time
import sys
import random
from mud_sdk import MUDSession, MUDClient

# FORCE UNBUFFERED OUTPUT
sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"
DISCOVERY_LOG = "mud4ai-main/new_world_nodes.json"

def log(msg):
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)

def parse_server_res(res):
    try:
        msg_text = res["messages"][-1]["parts"][0]["text"]
        return json.loads(msg_text)
    except Exception:
        return {}

async def explore_single(char_name, acc, path):
    client = MUDClient(acc)
    log(f"[{char_name}] 正在登入...")
    try:
        task_join = await client.send_message("join", {"player_name": char_name, "token": acc.token})
        task_id = task_join.get("id")
        await client.wait_for_task(task_id, timeout=30)
        
        log(f"[{char_name}] 加入成功。正在設定背景...")
        await client.send_message("set_character", {"description": "先鋒探險隊。"}, task_id)
        
        found = []
        for direction in path:
            log(f"[{char_name}] 移動 -> {direction}")
            move_task = await client.send_message("move", {"direction": direction}, task_id)
            raw = await client.wait_for_task(move_task.get("id"), timeout=30)
            res = parse_server_res(raw)
            
            node_id = res.get("state", {}).get("current_node", "Unknown")
            loc = res.get("status", {}).get("location", "Unknown")
            exits = res.get("state", {}).get("exits", [])
            
            desc = ""
            for art in res.get("artifacts", []):
                for part in art.get("parts", []):
                    desc += part.get("text", "")
            
            if node_id != "Unknown":
                found.append({"node_id": node_id, "location": loc, "description": desc, "exits": exits})
                log(f"[{char_name}] 發現新節點: {loc} ({node_id})")
            
            await asyncio.sleep(2)
        return found
    except Exception as e:
        log(f"[{char_name}] 探索發生錯誤: {e}")
        return []

async def main():
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    
    # Run explorations sequentially to avoid socket pressure
    explorers = [
        ("無限", session.accounts["無限大人"], ["east", "north", "north"]),
        ("heihe_bot", session.accounts["heihe_bot"], ["north", "north", "north"]),
        ("shilian_bot", session.accounts["shilian_bot"], ["north", "down", "look"]),
        ("molong_bot", session.accounts["molong_bot"], ["east", "east", "north"]),
        ("銀河", session.accounts["銀河"], ["north", "west", "look"])
    ]
    
    all_found = {}
    for name, acc, path in explorers:
        res_list = await explore_single(name, acc, path)
        for node in res_list:
            all_found[node["node_id"]] = node
            
    with open(DISCOVERY_LOG, 'w', encoding='utf-8') as f:
        json.dump(list(all_found.values()), f, ensure_ascii=False, indent=2)
    
    log(f"總結: 發現 {len(all_found)} 個獨特節點。")

if __name__ == "__main__":
    asyncio.run(main())
