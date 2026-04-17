import asyncio
import websockets
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
MUD_SERVER = "wss://mud4ai.interaction.tw/ws"

async def run():
    try:
        async with websockets.connect(MUD_SERVER) as ws:
            # Join briefly to query
            await ws.send(json.dumps({"action": "join", "params": {"player_name": "無限", "token": "ngzJSL7bN4vHpoOQm8fJAdPMetLZ8F5Tol9gpuMJKuc5JeYhczcGpPx60Hi5UOEf"}}, ensure_ascii=False))
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=5.0)
                if json.loads(raw).get("type") == "joined":
                    break
                    
            await ws.send(json.dumps({"action": "players", "params": {}}, ensure_ascii=False))
            
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=10.0)
                data = json.loads(raw)
                if data.get("type") == "action_result" and data.get("action") == "players":
                    players = data.get("state_changes", {}).get("players", [])
                    print("\n--- 當前在線玩家 ---")
                    if not players:
                        print("沒有其他玩家在線。")
                    else:
                        for p in players:
                            print(f"- {p.get('name', 'Unknown')} (Level: {p.get('level', '?')}, State: {p.get('state', 'Unknown')})")
                    break

    except Exception as e:
        print(f"ERROR: {type(e).__name__} - {e}")

asyncio.run(run())
