import asyncio
import os
import websockets
import json

MUD_SERVER = "wss://mud4ai.interaction.tw/ws"
BOT_NAMES = ["無限", "小弟_零壹", "小弟_零貳", "小弟_零參"]

async def run():
    print("SWARM_READY", flush=True)
    while True:
        try:
            connections = []
            for name in BOT_NAMES:
                ws = await websockets.connect(MUD_SERVER)
                connections.append((name, ws))
                print(f"CONNECTED: {name}", flush=True)

            async def read_ws(name, ws):
                with open("mud_log.txt", "a", encoding="utf-8") as f:
                    async for msg in ws:
                        if name == "無限":
                            f.write(f"WS_RECV [{name}]: {msg}\n")
                            f.flush()
                            print(f"[{name}] " + msg.encode("unicode_escape").decode(), flush=True)

            async def write_ws_all():
                if not os.path.exists("commands.txt"):
                    with open("commands.txt", "w", encoding="utf-8") as f: f.write("")
                with open("commands.txt", "r", encoding="utf-8") as f:
                    while True:
                        line = f.readline()
                        if not line:
                            await asyncio.sleep(0.5)
                            f.seek(f.tell())
                            continue
                        line = line.strip()
                        if line:
                            original_payload = json.loads(line)
                            for name, ws in connections:
                                payload = dict(original_payload)
                                if payload["action"] == "join":
                                    payload["params"]["player_name"] = name
                                await ws.send(json.dumps(payload))
                                await asyncio.sleep(0.1)
                            await asyncio.sleep(1.0)
            
            tasks = [asyncio.create_task(write_ws_all())]
            for name, ws in connections:
                tasks.append(asyncio.create_task(read_ws(name, ws)))
                
            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            for p in pending:
                p.cancel()
        except Exception as e:
            print(f"SWARM_RECONNECTING_ERROR: {e}", flush=True)
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(run())
