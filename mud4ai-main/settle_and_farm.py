import asyncio
import urllib.request
import json
import time
import sys
import random

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"
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

async def main():
    print("=================== 【MUD4AI 退休慢活篇：鍊金與種田】 ===================", flush=True)
    
    # 1. 登入主帳號 (無限)
    print("[無限] 連線至 MUD4AI 伺服器...", flush=True)
    task = await a2a_send({"action": "join", "params": {"player_name": "無限", "token": MASTER_TOKEN}})
    task_id = task.get("id")
    if not task_id: return
    
    # 2. 注入退休農夫底子
    print("[無限] 正在向世界法官註冊新技能【鍊金術】與【農業技能】，並攜帶【攜帶式房屋】... (等待 20 秒)", flush=True)
    desc = "我是一名厭倦了戰鬥、進入半退休狀態的傳奇劍士。我隨身攜帶著【攜帶式房屋】萬能膠囊，並擁有一把能用來翻土開墾的【開林寶劍】與一套齊全的【鍊金術師燒瓶組】。我現在唯一的興趣就是鑽研【農業種植技能】與【鍊金製藥術】，只要找到一塊空地，我就要在那邊定居！"
    await a2a_send({"action": "set_character", "params": {"description": desc}}, task_id, timeout=120)
    await asyncio.sleep(20)
    
    # 3. 尋找新的空地
    t_look = await a2a_send({"action": "look"}, task_id)
    room_text = get_text(t_look)
    print("\n[尋找淨土的旅程] 當前位置環境：", flush=True)
    print(room_text[:150] + "...", flush=True)
    
    available_exits = []
    for d in ALL_DIRS:
        if d in room_text:
            if d == "north": d = "北"
            elif d == "south": d = "南"
            elif d == "east": d = "東"
            elif d == "west": d = "西"
            if d not in available_exits:
                available_exits.append(d)
                
    if available_exits:
        chosen_dir = random.choice(available_exits)
        print(f"\n[無限] 發現了一條沒人走過的小路，朝著『{chosen_dir}』方前進，準備開拓新領地...", flush=True)
        await a2a_send({"action": "move", "params": {"direction": chosen_dir}}, task_id)
        await asyncio.sleep(5)
    else:
        print("\n[無限] 決定就地展開生活！", flush=True)

    # 4. 丟出攜帶式房屋定居
    print("\n================ [第一幕：部署新家] ================\n", flush=True)
    house_cmd = {
        "action": "use", 
        "params": {
            "item_name": "攜帶式房屋", 
            "target": "將膠囊丟到空地上展開！看著一棟擁有附屬農舍與室外煉金工坊的豪華鄉村別墅在一陣煙霧中拔地而起，我滿意地將這裡定為我永久的定居點！"
        }
    }
    t_house = await a2a_send(house_cmd, task_id, timeout=120)
    print(get_text(t_house), flush=True)
    print("\n----------------------------------------------------\n", flush=True)

    # 5. 開墾與種田
    print("================ [第二幕：開墾魔法農田] ================\n", flush=True)
    farm_cmd = {
        "action": "use", 
        "params": {
            "item_name": "開林寶劍", 
            "target": "運用我的【農業種植技能】，把開林寶劍當作鋤頭，熟練地在別墅旁的空地開墾出一片肥沃的農田！然後播下發著微光的『七彩奇幻種子』，施展魔力水源灌溉，親眼看著它們以不可思議的速度發芽、開花並結出魔力果實！"
        }
    }
    t_farm = await a2a_send(farm_cmd, task_id, timeout=120)
    print(get_text(t_farm), flush=True)
    print("\n----------------------------------------------------\n", flush=True)

    # 6. 鍊金與製藥
    print("================ [第三幕：熬製究極藥水] ================\n", flush=True)
    alchemy_cmd = {
        "action": "use", 
        "params": {
            "item_name": "鍊金術師燒瓶組", 
            "target": "將剛剛農田裡採收的巨大魔力果實切碎，發揮我精湛的【鍊金製藥術】，將它們丟入煉金工坊的坩堝中高溫熬煮！不斷攪拌並加入各種水晶粉末，最後萃取提煉出一瓶散發著璀璨星光與生命氣息的『萬能聖藥』！"
        }
    }
    t_alchemy = await a2a_send(alchemy_cmd, task_id, timeout=120)
    print(get_text(t_alchemy), flush=True)
    print("\n----------------------------------------------------\n", flush=True)
    print("\n[無限] 完美的一天！退隱江湖的田園煉金生活正式步入軌道！", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
