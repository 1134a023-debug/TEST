import json
import time

with open("commands.txt", "a", encoding="utf-8") as f:
    # 1. 習得技能並發動 10 房間連穿
    f.write(json.dumps({
        "action": "use", 
        "params": {
            "item_name": "萬能鑰匙", 
            "target": "強行登錄並習得【無限吸收】體質！接著啟動全自動尋路模式，在接下來的瞬間連續穿梭探索整整 10 個全新的未知房間地點（包含隱密神殿、地城秘境等），沿途【無限吸收】發動，將所見的任何神裝、道具、古代材料全部像黑洞一樣吸入背包中！"
        }
    }, ensure_ascii=False) + "\n")
    # 2. 顯示面板與道具
    f.write(json.dumps({"action": "status", "params": {}}, ensure_ascii=False) + "\n")
    f.write(json.dumps({"action": "inventory", "params": {}}, ensure_ascii=False) + "\n")

time.sleep(2)
