import json
import time
with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({"action": "take", "params": {"item_name": "古代文獻"}}, ensure_ascii=False) + "\n")
time.sleep(2)
