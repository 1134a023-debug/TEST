import json
import time

with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({
        "action": "use", 
        "params": {
            "item_name": "萬能鑰匙", 
            "target": "當前房間的實體生成器，強制在此區域額外生成三種精英怪物參與支線任務考驗：1.【虛數收割者】(能力：物理免疫，每次攻擊會隨機奪走玩家背包中的一件物品)，2.【熵之史萊姆】(能力：受到攻擊時會分裂成兩隻攻防翻倍的個體，無上限分裂)，3.【時間觀測者石像】(能力：會將戰鬥區域的時間流速調慢10倍，使所有非神級玩家的動作強制判定為失敗)。立刻生成並阻擋在此！"
        }
    }, ensure_ascii=False) + "\n")
    f.write(json.dumps({"action": "look", "params": {}}, ensure_ascii=False) + "\n")
    
time.sleep(3)
