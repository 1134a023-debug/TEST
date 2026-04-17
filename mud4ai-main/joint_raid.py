import asyncio
import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"

# 定義角色及其專屬技能背景
CHARS = {
    "無限": {
        "token": MASTER_TOKEN,
        "desc": "我是一名遊歷無數時空的劍士。我不破壞遊戲平衡地領悟了概念神技【無限】，這讓我在關鍵時刻能爆發出無限的可能性來看破並斬斷任何強大的存在。請配發【流浪者之劍】。",
        "action": {"action": "attack", "params": {"target": "發動神技【無限】！超越物理限制，直接對魔王防禦最薄弱的空間概念核心進行絕殺一擊！"}}
    },
    "黑河": {
        "token": "BNoZmUGk_FXvtQ1eGyHrdyi2YJvNwB8nlVhIYlhSL-5pUgRFEhlCUH6IsZSaNcdF",
        "desc": "我是堅不可摧的重裝盾衛。我擁有個別保護技【絕對防禦】以及群體保護技【群體挑釁】，發誓將所有敵人的攻擊吸引到自己身上，保護隊友。請配發【守護者大盾】。",
        "action": {"action": "examine", "params": {"target": "發動【群體挑釁】與【絕對防禦】！嘲諷房間內所有強大的魔物，並舉起大盾將所有對隊友的仇恨值集中在自己身上！"}}
    },
    "試煉": {
        "token": "swMZUQSxs_scdKmvJ3pmo3iBIxhKLTivLYiRi2KV3HncbmrZ_k3siVR25waAayOL",
        "desc": "我是隊伍中的尋路者與機關大師。我擁有被動技能【靈光一閃】，在面對複雜謎題或魔王機制時總能瞬間看破解法與破綻。請配發【先知放大鏡】。",
        "action": {"action": "examine", "params": {"target": "發動【靈光一閃】！快速觀察魔王的行動模式與房間內的機關聯動，大聲吶喊出破解魔王無敵狀態或弱點的關鍵解法給隊友聽！"}}
    },
    "魔龍": {
        "token": "GKagwh49e_ftd3fM8ZMErEa3qb3k2dyIhvJNcAYoonwA6HMDofpgTVrr8sr1qigC",
        "desc": "我是法師間的空中戰王者。我腦海中記載著完整的【全魔法圖鑑】，並且精通隱藏禁咒【六位合一】（融合冰火雷風光暗）。請配發【魔王法杖】。",
        "action": {"action": "attack", "params": {"target": "升空並翻開全魔法圖鑑，釋放隱藏禁咒【六位合一】！用六種元素的狂暴魔力融合轟炸整個區域！"}}
    }
}

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

async def setup_character(name, props):
    print(f"[{name}] Joining and generating character...", flush=True)
    task = await a2a_send({"action": "join", "params": {"player_name": name, "token": props["token"]}})
    task_id = task.get("id")
    if not task_id: return None
    
    await a2a_send({"action": "set_character", "params": {"description": props["desc"]}}, task_id, timeout=120)
    return task_id

async def main():
    print("=================== 【MUD4AI 聯合討伐副本】 ===================", flush=True)
    print("正在將四位神級角色連線，並進行技能與天賦覺醒設定...", flush=True)
    
    # 1. 喚醒所有角色
    tasks = {name: setup_character(name, props) for name, props in CHARS.items()}
    session_ids = {}
    for name, coro in tasks.items():
        session_ids[name] = await coro
    
    print("伺服器正在生成角色與專屬技能... (等待 20 秒)", flush=True)
    await asyncio.sleep(20)
    
    # 2. 所有人移動到同一個 Boss 房 (北邊)
    print("\n=================== 【集結與進軍】 ===================", flush=True)
    print("全員朝著『北方』的深淵副本前進...", flush=True)
    move_tasks = []
    for name, tid in session_ids.items():
        move_tasks.append(a2a_send({"action": "move", "params": {"direction": "北"}}, tid))
    await asyncio.gather(*move_tasks)
    await asyncio.sleep(5)
    
    # 3. 取得戰場環境 (由試煉洞察)
    print("\n=================== 【戰鬥階段一：洞察破綻】 ===================", flush=True)
    print("[試煉] (斥候) 正在使用【靈光一閃】偵查 Boss 機制...", flush=True)
    t_ex = await a2a_send(CHARS["試煉"]["action"], session_ids["試煉"], timeout=90)
    print(get_text(t_ex), flush=True)
    
    # 4. 黑河開啟群體嘲諷
    print("\n=================== 【戰鬥階段二：絕對守護】 ===================", flush=True)
    print("[黑河] (盾衛) 正在使用【群體挑釁】與【絕對防禦】吸收仇恨...", flush=True)
    t_taunt = await a2a_send(CHARS["黑河"]["action"], session_ids["黑河"], timeout=90)
    print(get_text(t_taunt), flush=True)
    
    # 5. 魔龍升空釋放禁咒
    print("\n=================== 【戰鬥階段三：魔法轟炸】 ===================", flush=True)
    print("[魔龍] (法師) 翻開【全魔法圖鑑】，開始詠唱隱藏禁咒【六位合一】...", flush=True)
    t_magic = await a2a_send(CHARS["魔龍"]["action"], session_ids["魔龍"], timeout=90)
    print(get_text(t_magic), flush=True)
    
    # 6. 無限發動神技絕殺
    print("\n=================== 【戰鬥階段四：概念破壞】 ===================", flush=True)
    print("[無限] (劍士) 拔出利刃，觸發概念神技【無限】，給予王最後一擊...", flush=True)
    t_slash = await a2a_send(CHARS["無限"]["action"], session_ids["無限"], timeout=90)
    print(get_text(t_slash), flush=True)
    
    print("\n=================== 【戰役結算面板】 ===================", flush=True)
    for name, tid in session_ids.items():
        t_stat = await a2a_send({"action": "status"}, tid)
        s_json = extract_status(get_text(t_stat))
        if s_json:
            print(f"[{name}] HP: {s_json.get('hp')}, Score: {s_json.get('score')}, Location: {s_json.get('location')}")
        else:
            print(f"[{name}] 無法取得結算資訊。")

if __name__ == "__main__":
    asyncio.run(main())
