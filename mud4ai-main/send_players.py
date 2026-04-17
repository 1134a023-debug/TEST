import json
import time

with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({"action": "players", "params": {}}, ensure_ascii=False) + "\n")

time.sleep(3)
