import json
with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({"action": "status", "params": {}}, ensure_ascii=False) + "\n")
    f.write(json.dumps({"action": "look", "params": {}}, ensure_ascii=False) + "\n")
