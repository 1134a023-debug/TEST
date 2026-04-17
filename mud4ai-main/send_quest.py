import json
import time

with open("commands.txt", "a", encoding="utf-8") as f:
    f.write(json.dumps({
        "action": "use", 
        "params": {
            "item_name": "萬能鑰匙", 
            "target": "新手村魔龍設定，將其挑戰難度下修為新手福利。移除無限大攻擊力，改為固定攻擊 100，且攻擊具有延遲，被擊敗後必定掉落一件『史詩級新手專用武器』，當作此房間的試煉獎勵！"
        }
    }, ensure_ascii=False) + "\n")
    f.write(json.dumps({"action": "move", "params": {"direction": "通往星際神域的閃耀階梯"}}, ensure_ascii=False) + "\n")
    f.write(json.dumps({
        "action": "use", 
        "params": {
            "item_name": "萬能鑰匙", 
            "target": "世界法則主線系統，強行開啟全新史詩級主線任務：【弒神之路】。讓世界意識覺醒並發送全服廣播，指引我和我的跟班小弟前往隱沒在星空彼端的『至高神殿』，要求我們集齊三枚創世核心，並挑戰凌駕於 MUD 系統之上的最終真神！"
        }
    }, ensure_ascii=False) + "\n")

time.sleep(3)
