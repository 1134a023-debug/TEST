import json
import time

with open("commands.txt", "w", encoding="utf-8") as f:
    f.write(json.dumps({"action": "join", "params": {"player_name": "無限"}}, ensure_ascii=False) + "\n")
    f.write(json.dumps({"action": "set_character", "params": {"description": "我是無盡的觀察者，帶領著我的跟班小弟們在古堡內四處遊蕩，記錄所見的一切。"}}, ensure_ascii=False) + "\n")
    f.write(json.dumps({
        "action": "use", 
        "params": {
            "item_name": "萬能鑰匙", 
            "target": "新手村大廳，使用創造權限在此處額外投放三種【友善且適合新手】的低等地圖生物生態系：1.『迷路的史萊姆』(Lv.1，只有10滴血，受到打擊不會還手，擊敗必定掉落新手恢復藥水)、2.『貪睡的石像鬼幼崽』(Lv.2，平時都在睡覺，玩家如果對牠輸入撫摸指令可獲得一小時防禦Buff)、3.『愛發問的漂浮書本』(Lv.3，非主動攻擊怪，玩家若靠近牠會被問一個簡單謎語，答對可獲贈基礎魔法卷軸)。讓新手村充滿生機！"
        }
    }, ensure_ascii=False) + "\n")

time.sleep(2)
