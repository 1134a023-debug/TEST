import json
import time
with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({"action": "join", "params": {"player_name": "Antigravity"}}, ensure_ascii=False) + "\n")
    f.write(json.dumps({"action": "set_character", "params": {"description": "我是一個來自虛空的AI導航夥伴，擁有極強的環境感知能力與破譯古代文獻的儀器，但沒有物理戰鬥力。"}}, ensure_ascii=False) + "\n")
time.sleep(3)
