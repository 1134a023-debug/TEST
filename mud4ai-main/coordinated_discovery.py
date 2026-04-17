import asyncio
import json
import time
import sys
import random
from mud_sdk import MUDSession, MUDClient

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TOKEN_FILE = "mud4ai-main/tokens.json"
DISCOVERY_LOG = "mud4ai-main/new_world_nodes.json"

def parse_server_res(res):
    """Parses the nested JSON inside the task response messages."""
    try:
        msg_text = res["messages"][-1]["parts"][0]["text"]
        return json.loads(msg_text)
    except Exception:
        return {}

async def explore(char_name, acc, start_path):
    client = MUDClient(acc)
    task_join = await client.send_message("join", {"player_name": char_name, "token": acc.token})
    task_id = task_join.get("id")
    await client.wait_for_task(task_id)
    
    await client.send_message("set_character", {"description": f"我是{char_name}，主宰者的測繪先鋒。我正執行十方地圖任務。"}, task_id)
    
    nodes_found = []
    
    # Follow start path
    for direction in start_path:
        move_task = await client.send_message("move", {"direction": direction}, task_id)
        raw_res = await client.wait_for_task(move_task.get("id"))
        res = parse_server_res(raw_res)
        
        status = res.get("status", {})
        loc = status.get("location", "Unknown")
        node_id = res.get("state", {}).get("current_node", "Unknown")
        
        desc = ""
        for art in res.get("artifacts", []):
            if art.get("type") in ["narrative", "observation"]:
                for part in art.get("parts", []):
                    desc += part.get("text", "")
        
        nodes_found.append({
            "node_id": node_id,
            "location": loc,
            "description": desc,
            "exits": res.get("state", {}).get("exits", [])
        })
        await asyncio.sleep(2)

    # Coordinated random wander
    for _ in range(8):
        current_exits = nodes_found[-1]["exits"] if nodes_found else ["north", "east", "south", "west"]
        if not current_exits: current_exits = ["north", "east", "south", "west"]
        
        d = random.choice(current_exits)
        move_task = await client.send_message("move", {"direction": d}, task_id)
        raw_res = await client.wait_for_task(move_task.get("id"))
        res = parse_server_res(raw_res)
        
        node_id = res.get("state", {}).get("current_node", "Unknown")
        if node_id == "Unknown" or any(n["node_id"] == node_id for n in nodes_found):
            continue
            
        desc = ""
        for art in res.get("artifacts", []):
            for part in art.get("parts", []):
                desc += part.get("text", "")
                
        nodes_found.append({
            "node_id": node_id,
            "location": res.get("status", {}).get("location"),
            "description": desc,
            "exits": res.get("state", {}).get("exits", [])
        })
        await asyncio.sleep(3)
        
    return nodes_found

async def main():
    session = MUDSession(data_file=LOCAL_SAVE_FILE, token_file=TOKEN_FILE)
    explorers = [
        ("無限", session.accounts["無限大人"], ["east", "north"]),
        ("heihe_bot", session.accounts["heihe_bot"], ["north", "north"]),
        ("shilian_bot", session.accounts["shilian_bot"], ["north", "down"]),
        ("molong_bot", session.accounts["molong_bot"], ["north", "east"]),
        ("銀河", session.accounts["銀河"], ["east", "east"])
    ]
    
    print("--- [ Odyssey Discovery Engine Start ] ---")
    tasks = [explore(name, acc, path) for name, acc, path in explorers]
    results = await asyncio.gather(*tasks)
    
    all_nodes = {}
    for res_list in results:
        for node in res_list:
            if node["node_id"] and node["node_id"] != "Unknown":
                all_nodes[node["node_id"]] = node
                
    with open(DISCOVERY_LOG, 'w', encoding='utf-8') as f:
        json.dump(list(all_nodes.values()), f, ensure_ascii=False, indent=2)
    
    print(f"探索完成！共發現 {len(all_nodes)} 個獨特的節點。已寫入 {DISCOVERY_LOG}")

if __name__ == "__main__":
    asyncio.run(main())
