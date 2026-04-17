import asyncio
import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"

AWAKENINGS = [
    {
        "name": "無限",
        "token": MASTER_TOKEN,
        "desc": "我是一名遊歷無數時空的劍士，我發誓絕不破壞遊戲平衡地領悟了神技【無限】。如今我正在閉關，試圖突破瓶頸，將技能磨練到絕對覺醒的領域！",
        "trigger": "【極限突破】我將所有的精神與肉體力量注入手中的流浪者之劍！我的概念神技【無限】突破了最後的極限，正式進化為覺醒技能：【無限・終焉切斷】！周圍的空間被這股劍氣切碎，請描述這場天地異象與我覺醒後散發出的無敵力量！"
    },
    {
        "name": "黑河",
        "token": "BNoZmUGk_FXvtQ1eGyHrdyi2YJvNwB8nlVhIYlhSL-5pUgRFEhlCUH6IsZSaNcdF",
        "desc": "我是堅不可摧的重裝盾衛。我擁有個別保護技【絕對防禦】以及群體保護技【群體挑釁】。我正在接受千錘百鍊的肉體苦行，試圖邁向覺醒！",
        "trigger": "【鐵血覺醒】我將守護者大盾深深砸入地面，仰天長嘯！我的防禦技巧與挑釁本能完美融合，正式進化為覺醒狀態：【絕對領域・不滅金身】！一道堅不可摧的黃金結界籠罩全場，請描述這股連神明都無法擊破的守護氣場！"
    },
    {
        "name": "試煉",
        "token": "swMZUQSxs_scdKmvJ3pmo3iBIxhKLTivLYiRi2KV3HncbmrZ_k3siVR25waAayOL",
        "desc": "我是隊伍中的尋路者與機關大師。我擁有被動技能【靈光一閃】。我正在一個充滿古代符文的房間進行無限演算，試圖讓大腦覺醒！",
        "trigger": "【真理降臨】我的大腦在一瞬間處理了上億兆次的演算，靈光一閃昇華為全知全能的境界！我正式覺醒被動神技：【全知之眼・真理領域】！世界的源代碼與魔物的致命弱點在我眼中化為發光的細線，請描述這洞穿一切的智慧異象！"
    },
    {
        "name": "魔龍",
        "token": "GKagwh49e_ftd3fM8ZMErEa3qb3k2dyIhvJNcAYoonwA6HMDofpgTVrr8sr1qigC",
        "desc": "我是法師間的空中戰王者。我腦海中記載著【全魔法圖鑑】與禁咒【六位合一】。我正在元素風暴的最中心冥想，試圖撕裂魔力核心完成覺醒！",
        "trigger": "【魔道巔峰】我高舉魔王法杖，強行將冰火雷風光暗六種元素全部捏碎、甚至融合理想與現實！六位合一正式覺醒為最終禁咒：【創世禁咒・元素崩壞】！這是一股能重塑世界規則的磅礡魔力，請描述這毀滅與重生交織的神話級場面！"
    }
]

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

async def process_awakening(char):
    name = char['name']
    print(f"\n=================== 【 {name} 覺醒儀式 】 ===================", flush=True)
    
    # Join
    t_join = await a2a_send({"action": "join", "params": {"player_name": name, "token": char["token"]}})
    task_id = t_join.get("id")
    if not task_id: 
        print(f"[{name}] 無法連線伺服器。", flush=True)
        return
    
    # Set background
    print(f"[{name}] 啟動極限冥想狀態 (等待生成)...", flush=True)
    full_desc = char["desc"] + " 為了突破，我手握著傳說中的道具『覺醒之石』準備發動絕技。"
    await a2a_send({"action": "set_character", "params": {"description": full_desc}}, task_id, timeout=120)
    await asyncio.sleep(15)
    
    # Trigger Awakening
    print(f"[{name}] 💥 突破極限！發動覺醒宣言：\n「{char['trigger']}」\n", flush=True)
    use_cmd = {
        "action": "use",
        "params": {
            "item_name": "覺醒之石",
            "target": char['trigger']
        }
    }
    t_awaken = await a2a_send(use_cmd, task_id, timeout=120)
    print("\n[ 傳奇怪物及世界意志的回應 ]\n", flush=True)
    print(get_text(t_awaken), flush=True)

async def main():
    print("即將為四位傳奇玩家啟動【技能覺醒】異象生成...", flush=True)
    for c in AWAKENINGS:
        await process_awakening(c)
    print("所有角色的終極覺醒已經完成！", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
