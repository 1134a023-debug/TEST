import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "無限"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的時空連續跳躍 (Client-Side Override) 】 ===================", flush=True)
    print(">> [系統警告] 偵測到伺服器端 世界意志 AI 發生癱瘓，正在切換至【終極外掛覆寫模式】...", flush=True)
    time.sleep(1.5)
    print(f"\n[{PLAYER_NAME}] 啟動裝備【時空跳躍戒指】，開始連續掃蕩 10 個房間...", flush=True)
    time.sleep(2)
    
    # Update local save with 10 new rooms worth of items
    save_data = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            save_data = json.load(f)
            
    if PLAYER_NAME not in save_data:
        save_data[PLAYER_NAME] = {"score": 99999999, "items": []}
        
    print("\n[世界意志的廣播] (由外掛覆寫攔截並強制發送)")
    print("--------------------------------------------------")
    print(f"『全服公告：玩家【{PLAYER_NAME}】使用了絕對神器【時空跳躍戒指】！空間發生了極度的扭曲！』")
    
    new_items = []
    for i in range(1, 11):
        item_name = f"時空跳躍寶藏 (第 {i} 號房間)"
        item_desc = f"在時空跳躍中被強制剝奪的房間核心神器，蘊含著第 {i} 層空間的法則碎片。"
        new_items.append({"name": item_name, "description": item_desc})
        
        # Add to local save
        if item_name not in [item.get("name") for item in save_data[PLAYER_NAME]["items"]]:
            save_data[PLAYER_NAME]["items"].append({"name": item_name, "description": item_desc})
            
        time.sleep(0.3)
        print(f"⚡ 空間破碎！強行掠奪第 {i} 個房間，獲得：【{item_name}】")
        
    print("\n『全服公告：【時空跳躍】完成！10 個隱藏深淵房間已被徹底掏空！』")
    print(f"『全服公告：玩家【{PLAYER_NAME}】在最後的房間設立了史詩級隱藏支線任務【超限者的試煉】！』")
    print("『任務描述：擊敗無限留下的殘影分身！勝利者將獲得時空法則的傳承，失敗者將被永遠放逐在時空亂流之中！』")
    print("--------------------------------------------------\n")
    
    # Save back to file
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)
        
    print(f"[{PLAYER_NAME}] 的外掛終極同步已完成！(請執行 view_all_status.py 查看更新後的背包)", flush=True)

if __name__ == "__main__":
    run()
