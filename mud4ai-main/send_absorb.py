import json
import time

with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({
        "action": "use", 
        "params": {
            "item_name": "萬能鑰匙", 
            "target": "世界網絡，強行啟動廣域精神連結，掃描並吸收當前所有在線玩家的技能、記憶與專長，綜合至無限的庫中，隨後在前方強行劈開一扇通往廣闊大世界（開放世界）的維度傳送門！"
        }
    }, ensure_ascii=False) + "\n")
    f.write(json.dumps({"action": "move", "params": {"direction": "傳送門"}}, ensure_ascii=False) + "\n")

time.sleep(2)
