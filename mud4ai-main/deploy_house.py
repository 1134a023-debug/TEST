import asyncio
import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

MASTER_TOKEN = "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"

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
    print("===================================================", flush=True)
    print("【萬能膠囊系統啟動】：準備創造並部署 [攜帶式房屋]...", flush=True)
    print("===================================================\n", flush=True)
    
    # 1. 登入主帳號 (無限)
    print("[無限] 連線至 MUD4AI 伺服器...", flush=True)
    task = await a2a_send({"action": "join", "params": {"player_name": "無限", "token": MASTER_TOKEN}})
    task_id = task.get("id")
    if not task_id: return
    
    # 2. 注入背景，獲得道具
    print("[無限] 正在向世界法官註冊新道具【攜帶式房屋】... (等待 20 秒)", flush=True)
    desc = "我是一名遊歷無數時空的旅行者。我隨身攜帶著一個由高級空間科技與魔法混合製成的神物：【攜帶式房屋】萬能膠囊，只要將它丟在地上，就能隨時隨地展開成一棟內部極致奢華、擁有廚房與溫泉的度假別墅，讓我在任何惡劣的地下城都能獲得最頂級的休息與全面恢復！"
    await a2a_send({"action": "set_character", "params": {"description": desc}}, task_id, timeout=120)
    await asyncio.sleep(20)
    
    # 3. 查看周遭環境
    t_look = await a2a_send({"action": "look"}, task_id)
    print("\n[當前環境]:", flush=True)
    print(get_text(t_look), flush=True)
    
    # 4. 丟出攜帶式房屋並使用！
    print("\n[無限] 丟出萬能膠囊，發動道具：【攜帶式房屋】！", flush=True)
    use_cmd = {
        "action": "use", 
        "params": {
            "item_name": "攜帶式房屋", 
            "target": "將膠囊丟到空地上展開！走進這棟豪華的隨身別墅，泡進溫暖的室內溫泉中洗去所有疲憊，喝下吧台自動調製的精靈之酒，將血量與魔力全數恢復到滿點，並安穩地睡上一覺！"
        }
    }
    t_use = await a2a_send(use_cmd, task_id, timeout=120)
    print("\n================ [劇情生成結果] ================\n", flush=True)
    print(get_text(t_use), flush=True)
    print("================================================\n", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
