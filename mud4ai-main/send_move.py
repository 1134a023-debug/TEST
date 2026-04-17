import json
import time

with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({"action": "move", "params": {"direction": "north"}}, ensure_ascii=False) + "\n")

# Wait a moment for ws_bridge to process it and server to reply
time.sleep(2)
