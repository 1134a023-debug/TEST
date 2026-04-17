import json
import time

with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({
        "action": "use", 
        "params": {
            "item_name": "萬能鑰匙", 
            "target": "當前的房間空間，發動神級改寫：在此地設下絕對無法迴避的【無限魔龍的考驗】強制支線任務。任何踏入此房間的其他玩家，都將立刻遭遇一頭攻擊力界於 100 到 無限大 (∞) 不等、擁有毀滅吐息的『終焉魔龍』。若是無法戰勝或獻上頂級神器，將永遠被困在這間房間遭受無盡的折磨！"
        }
    }, ensure_ascii=False) + "\n")

time.sleep(3)
