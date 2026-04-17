import asyncio
import os
import websockets
import json

MUD_SERVER = "wss://mud4ai.interaction.tw/ws"

async def run():
    print("WS_READY", flush=True)
    
    while True:
        try:
            async with websockets.connect(MUD_SERVER) as ws:
                print("CONNECTED", flush=True)
                
                async def read_ws():
                    with open("mud_log.txt", "w", encoding="utf-8") as f: f.write("") # Clear log on reconnect
                    with open("mud_log.txt", "a", encoding="utf-8") as f:
                        async for msg in ws:
                            f.write(f"WS_RECV: {msg}\n")
                            f.flush()
                            print(msg.encode("unicode_escape").decode(), flush=True)
                            
                async def write_ws():
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
                                await ws.send(line)
                                await asyncio.sleep(1.0) # Delay to avoid spamming
                        
                done, pending = await asyncio.wait(
                    [asyncio.create_task(read_ws()), asyncio.create_task(write_ws())],
                    return_when=asyncio.FIRST_COMPLETED
                )
                for p in pending:
                    p.cancel()
        except Exception as e:
            print(f"WS_RECONNECTING_ERROR: {e}", flush=True)
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(run())
