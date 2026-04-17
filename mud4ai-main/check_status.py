import asyncio
import websockets
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

MUD_SERVER = "wss://mud4ai.interaction.tw/ws"

async def run():
    try:
        async with websockets.connect(MUD_SERVER) as ws:
            print("SENDING join", flush=True)
            await ws.send(json.dumps({"action": "join", "params": {"player_name": "無限", "token": "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"}}, ensure_ascii=False))
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=5.0)
                if json.loads(raw).get("type") == "joined":
                    break
                    
            print("SENDING set_character", flush=True)
            act_char = {"action": "set_character", "params": {"description": "我是GM『無限』，全屬性皆為無上限，無敵狀態！"}}
            await ws.send(json.dumps(act_char, ensure_ascii=False))
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=45.0)
                d = json.loads(raw)
                if d.get("type") == "action_result" and d.get("action") == "set_character":
                    print("Character Set Complete.", flush=True)
                    break
            
            print("\n--- 屬性面板 (STATUS) ---", flush=True)
            await ws.send(json.dumps({"action": "status", "params": {}}, ensure_ascii=False))
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=10.0)
                d = json.loads(raw)
                if d.get("type") not in ["broadcast", "world_whisper", "world_event", "quest_assigned", "seal_pulse"]:
                    print(json.dumps(d, ensure_ascii=False, indent=2), flush=True)
                    break
                    
            print("\n--- 背包面板 (INVENTORY) ---", flush=True)
            await ws.send(json.dumps({"action": "inventory", "params": {}}, ensure_ascii=False))
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=10.0)
                d = json.loads(raw)
                if d.get("type") not in ["broadcast", "world_whisper", "world_event", "quest_assigned", "seal_pulse"]:
                    print(json.dumps(d, ensure_ascii=False, indent=2), flush=True)
                    break

    except Exception as e:
        print("ERROR:", type(e).__name__, e, flush=True)

asyncio.run(run())
