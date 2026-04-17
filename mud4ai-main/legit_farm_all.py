import asyncio
import urllib.request
import json
import time
import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"

CHARS = [
    {
        "name": "無限",
        "token": MASTER_TOKEN,
        "pref_dir": "北",
        "desc": "我是一名來自遠方的流浪劍士，踏上旅程是為了尋找失落的古堡秘密，個性堅定且善於觀察。"
    },
    {
        "name": "黑河",
        "token": "BNoZmUGk_FXvtQ1eGyHrdyi2YJvNwB8nlVhIYlhSL-5pUgRFEhlCUH6IsZSaNcdF",
        "pref_dir": "東",
        "desc": "我是一名沉默寡言的盾衛，為了保護同伴不惜一切，喜歡四處探索與收集物資。"
    },
    {
        "name": "試煉",
        "token": "swMZUQSxs_scdKmvJ3pmo3iBIxhKLTivLYiRi2KV3HncbmrZ_k3siVR25waAayOL",
        "pref_dir": "南",
        "desc": "我是一名靈動的斥候，擅長解開機關與謎題，總是試圖從NPC口中套出情報。"
    },
    {
        "name": "魔龍",
        "token": "GKagwh49e_ftd3fM8ZMErEa3qb3k2dyIhvJNcAYoonwA6HMDofpgTVrr8sr1qigC",
        "pref_dir": "西",
        "desc": "我是一位狂野的法師學徒，對世界充滿好奇，遇到什麼都會試著用魔法探查一番。"
    }
]

OPPOSITE_DIR = {"北": "南", "南": "北", "東": "西", "西": "東", "上": "下", "下": "上"}
ALL_DIRS = ["北", "南", "東", "西", "上", "下", "north", "south", "east", "west"]

def a2a_req(action, task_id=None, timeout=60):
    msg = {"messageId": f"msg-{id(action)}_{time.time()}", "role": "user",
           "parts": [{"kind": "text", "text": json.dumps(action)}]}
    if task_id:
        msg["taskId"] = task_id
    req = urllib.request.Request(
        "https://mud4ai.interaction.tw/a2a",
        data=json.dumps({"jsonrpc": "2.0", "method": "SendMessage", "id": "1", "params": {"message": msg}}).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    try:
        res = urllib.request.urlopen(req, timeout=timeout)
        parsed = json.loads(res.read().decode('utf-8'))
        return parsed.get("result", {}).get("task", {})
    except BaseException:
        return {}

async def a2a_send(action, task_id=None, timeout=60):
    return await asyncio.to_thread(a2a_req, action, task_id, timeout)

def get_text(t):
    out = ""
    for a in t.get("artifacts", []):
        for p in a.get("parts", []):
            text = p.get('text', '')
            if text.strip(): out += text + "\n"
    return out

def extract_status(text):
    for line in text.split('\n'):
        if line.strip().startswith('{"hp":'):
            try: return json.loads(line.strip())
            except: pass
    return None

def extract_inventory(text):
    inv_json = []
    for line in text.split('\n'):
        if line.strip().startswith('[state:'):
            try:
                jstr = line.strip()[7:-1].strip()
                inv_json = json.loads(jstr).get('inventory', [])
            except: pass
    return inv_json

async def legit_bot(char):
    name = char['name']
    pref = char['pref_dir']
    
    print(f"[{name}] Connecting... (Roleplay mode, Target: {pref})", flush=True)
    task = await a2a_send({"action": "join", "params": {"player_name": name, "token": char["token"]}})
    task_id = task.get("id")
    if not task_id: return
    
    print(f"[{name}] Generating Normal Character (waiting 30s)...", flush=True)
    await a2a_send({"action": "set_character", "params": {"description": char["desc"]}}, task_id, timeout=120)
    await asyncio.sleep(30)
    
    last_dir = None
    step = 0
    max_steps = 30
    final_s_json = None
    final_inv_json = []

    while step < max_steps:
        step += 1
        print(f"\n[{name} - Step {step}] Exploring naturally...", flush=True)
        
        # 1. Look
        t_look = await a2a_send({"action": "look"}, task_id)
        room_text = get_text(t_look)
        
        # 2. Examine the room for clues
        print(f"[{name}] Examining environment carefully...", flush=True)
        t_exam = await a2a_send({"action": "examine", "params": {"target": "房間內所有可疑的角落、雕像機關或是留下來的線索"}}, task_id)
        room_text += "\n" + get_text(t_exam)
        
        # 3. Take items if any mentioned
        print(f"[{name}] Attempting to take useful items...", flush=True)
        await a2a_send({"action": "take", "params": {"item_name": "任何發光或有價值的任務物品"}}, task_id)
        
        # 4. Talk to NPCs
        print(f"[{name}] Talking to whoever is present...", flush=True)
        await a2a_send({"action": "talk", "params": {"npc_name": "房間內的任何人", "message": "您好，請問關於大沉寂的真相或是接下來的路該怎麼走，您有什麼頭緒嗎？"}}, task_id)
        
        # 5. Check Score to see if quest advanced
        t_status = await a2a_send({"action": "status"}, task_id)
        s_json = extract_status(get_text(t_status))
        if s_json:
            final_s_json = s_json
            if s_json.get("score", 0) > 0:
                print(f"[{name}] =============> QUEST ADVANCED LEGITIMATELY! Score: {s_json['score']} <=============", flush=True)
                break
                
        # Parse Exits
        available_exits = []
        for d in ALL_DIRS:
            if d in room_text:
                if d == "north": d = "北"
                elif d == "south": d = "南"
                elif d == "east": d = "東"
                elif d == "west": d = "西"
                if d not in available_exits:
                    available_exits.append(d)
                    
        # Filter backward steps if possible
        if len(available_exits) > 1 and last_dir and OPPOSITE_DIR.get(last_dir) in available_exits:
            available_exits.remove(OPPOSITE_DIR[last_dir])
            
        if not available_exits:
            available_exits = ["北", "南", "東", "西"] # Fallback
            
        chosen_dir = pref if pref in available_exits else random.choice(available_exits)
        last_dir = chosen_dir
        
        print(f"[{name}] Detected Exits: {available_exits}. Moving {chosen_dir} ...", flush=True)
        await a2a_send({"action": "move", "params": {"direction": chosen_dir}}, task_id)
        await asyncio.sleep(5)
        
    print(f"[{name}] Completed {step} exploration steps.", flush=True)
    
    # Get Final Inventory
    t_inv = await a2a_send({"action": "inventory"}, task_id)
    final_inv_json = extract_inventory(get_text(t_inv))
    
    print(f"\n================= {name} 的最終狀態面板 =================", flush=True)
    if final_s_json:
        print(f"🔹 **等級/稱號**: {name}", flush=True)
        print(f"❤️ **血量 (HP)**: {final_s_json.get('hp')}", flush=True)
        print(f"🏆 **總積分 (Score)**: {final_s_json.get('score')} 分", flush=True)
        print(f"📍 **當前位置**: {final_s_json.get('location')}", flush=True)
    print(f"🎒 **背包物品 ({len(final_inv_json)} 件)**: ", flush=True)
    if final_inv_json:
        for i, item in enumerate(final_inv_json):
            print(f"  {i+1}. 【{item.get('name')}】 - {item.get('description')}", flush=True)
    else: print("  (空)", flush=True)
    print("=====================================================\n", flush=True)

async def main():
    print("🚀 STARTING LEGITIMATE RPG MULTI-BOT (MAX 30 STEPS)...", flush=True)
    tasks = [legit_bot(c) for c in CHARS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
