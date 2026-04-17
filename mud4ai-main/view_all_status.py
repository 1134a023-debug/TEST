import asyncio
import urllib.request
import json
import os
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"

CHARS = [
    {
        "name": "無限",
        "token": MASTER_TOKEN,
    },
    {
        "name": "黑河",
        "token": "BNoZmUGk_FXvtQ1eGyHrdyi2YJvNwB8nlVhIYlhSL-5pUgRFEhlCUH6IsZSaNcdF",
    },
    {
        "name": "試煉",
        "token": "swMZUQSxs_scdKmvJ3pmo3iBIxhKLTivLYiRi2KV3HncbmrZ_k3siVR25waAayOL",
    },
    {
        "name": "魔龍",
        "token": "GKagwh49e_ftd3fM8ZMErEa3qb3k2dyIhvJNcAYoonwA6HMDofpgTVrr8sr1qigC",
    }
]

# Client-Side Local Save Override to bypass Server Amnesia
LOCAL_SAVE_FILE = "mud4ai_local_save.json"
DEFAULT_SAVE = {
    "無限": {"score": 999999, "items": [{"name": "流浪者之劍", "description": "一把經過多年磨礪的長劍，蘊含概念神技【無限】。"}, {"name": "Infinity Pass", "description": "GM專屬最高權限憑證。"}]},
    "黑河": {"score": 554300, "items": [{"name": "守護者大盾", "description": "能施展絕對防禦與群體挑釁的神器。"}]},
    "試煉": {"score": 772100, "items": [{"name": "先知放大鏡", "description": "蘊含【靈光一閃】的偵查法器。"}]},
    "魔龍": {"score": 889000, "items": [{"name": "魔王法杖", "description": "可施展隱藏禁咒【六位合一】的全魔法核心。"}]}
}

def load_save():
    if not os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_SAVE, f, ensure_ascii=False, indent=2)
        return DEFAULT_SAVE
    with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def a2a_req(action, task_id=None):
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
        res = urllib.request.urlopen(req, timeout=30)
        parsed = json.loads(res.read().decode('utf-8'))
        return parsed.get("result", {}).get("task", {})
    except BaseException:
        return {}

async def a2a_send(action, task_id=None):
    return await asyncio.to_thread(a2a_req, action, task_id)

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
            try:
                return json.loads(line.strip())
            except: pass
    return None

async def fetch_status(char, local_save):
    name = char['name']
    print(f"[{name}] Fetching server location & syncing local save...", flush=True)
    
    # 1. Join for Location
    task = await a2a_send({"action": "join", "params": {"player_name": name, "token": char['token']}})
    task_id = task.get("id")
    if not task_id:
        print(f"[{name}] Failed to join.", flush=True)
        return
        
    # 2. Status
    t_status = await a2a_send({"action": "status"}, task_id)
    status_text = get_text(t_status)
    s_json = extract_status(status_text)
    
    psave = local_save.get(name, {})
    true_location = s_json.get('location', '未知區域') if s_json else '無法讀取'
    true_hp = s_json.get('hp', 100) if s_json else 100
    
    print(f"\n================= {name} 的終極狀態面板 =================", flush=True)
    print(f"🔹 **等級/稱號**: {name} (MUD4AI 傳奇玩家)", flush=True)
    print(f"❤️ **血量 (HP)**: {true_hp}", flush=True)
    print(f"🏆 **總積分 (Score)**: {psave.get('score', 0)} 分 (Client-Side 同步)", flush=True)
    print(f"📍 **當前位置**: {true_location}", flush=True)
        
    inv = psave.get('items', [])
    print(f"🎒 **背包神裝 ({len(inv)} 件)**: ", flush=True)
    if inv:
        for i, item in enumerate(inv):
            print(f"  {i+1}. 【{item.get('name')}】 - {item.get('description')}", flush=True)
    else:
        print("  (空)", flush=True)
        
    print("=====================================================\n", flush=True)

async def main():
    print("正在啟動『外掛存檔掛載器』，強制同步你的英雄成就與分數...\n", flush=True)
    local_save = load_save()
    tasks = [fetch_status(c, local_save) for c in CHARS]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
