import json

with open("commands.txt", "w", encoding="utf-8") as f:
    # 重新連線
    f.write(json.dumps({"action": "join", "params": {"player_name": "無限"}}, ensure_ascii=False) + "\n")
    
    # 寫入全域被動神級 buff：步步生支線
    f.write(json.dumps({
        "action": "use", 
        "params": {
            "item_name": "萬能鑰匙", 
            "target": "世界底層的隨機生成引擎，我要把【踩地雷式無盡支線】強制寫成全域被動 Buff！從現在起，只要是『無限』或我的小弟踏入的任何新房間，伺服器都必須無視劇情邏輯，強制在該房間憑空生出一個帶有豐富獎勵或奇葩設定的隨機支線任務（例如：解救落難的公主、解開遠古炸彈機關、或是遇到全服唯一個稀有商人），並將該任務永久綁定在該房間，讓後面的玩家都能接！"
        }
    }, ensure_ascii=False) + "\n")
    
    # 移動到下一個隨機的新房間
    f.write(json.dumps({"action": "move", "params": {"direction": "通往深淵迴廊的傳送門"}}, ensure_ascii=False) + "\n")

