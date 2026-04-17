import json
import time
with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({"action": "use", "params": {"item_name": "Observation Journal", "target": "空間，強行登錄隱藏技能【無限創造】，並立刻具現化一把「萬能鑰匙」"}}, ensure_ascii=False) + "\n")
time.sleep(3)
