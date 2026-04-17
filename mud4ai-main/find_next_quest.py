import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的神級新手冒險：無限的真正遺產 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    if PLAYER_NAME not in saves:
        print("未找到存檔！")
        return
        
    char_data = saves[PLAYER_NAME]
    
    print(f"📍 {PLAYER_NAME} 站在【焦黑的地下城王座】，回想起先前擊敗殘影時的異狀。")
    print("「無限前輩留下來的考驗，真的只有區區一場戰鬥嗎？」")
    time.sleep(2)
    
    print(f"\n🥣 {PLAYER_NAME} 決定喝下剛剛烹調的神級料理：【向神明許願(料理)】！")
    time.sleep(1.5)
    print("✨ 一陣黃金般的光芒籠罩了 銀河 的全身，系統提示：【逆天好運】狀態已附加 (持續 24 小時)！")
    time.sleep(1.5)
    
    print(f"\n💍 藉著極致的好運加持，{PLAYER_NAME} 再次轉動了【時空跳躍戒指(核心)】，回到了：")
    print("🌪️ 【被徹底掠奪的空間 (原深淵第 7 房間)】")
    time.sleep(2)
    
    print("\n🔍 發動被動技能【按部就班】，銀河 開始對這個被掏空的房間進行地毯式搜索。")
    print("幸運值拉滿的情況下，【幸運手杖】突然發出了高頻的震鳴！")
    time.sleep(2)
    
    print("\n壁面那句囂張的刻字『無限 大人到此一遊，寶藏我全拿走了哈哈哈哈！』開始發生扭曲。")
    print("字體剝落，底下的代碼重新排列，竟然形成了一個隱藏的光學投影面板！")
    time.sleep(2.5)
    
    print("\n『真正的試煉，隱藏在虛無之中。』")
    print("投影面板中傳出 無限 懶洋洋但充滿威嚴的語音留言：")
    print("『喲，能找到這裡，代表你已經擊敗了我的測試版分身，而且運氣還不錯。』")
    print("『這世界上所有的寶物對我來說已經沒有意義。如果你渴望得到我真正遺留下來的【創世管理員權限 (GM Core)】...』")
    print("『那就去收集散落在維度裂縫中的四把【邏輯鎖鑰】吧。』")
    time.sleep(4)
    
    print("\n『第一把鑰匙，我把它丟在了一個連時間都會被凍結的地方：【絕對零度的冰霜迴廊】。』")
    print("『前提是，別在那裡被凍成代碼碎片啊，超限者。我們終點見。』")
    time.sleep(2)
    
    quest_log = {"quest_name": "無限的真正遺產 (連續任務)", "status": "進行中", "target": "尋找第一把邏輯鎖鑰", "location": "絕對零度的冰霜迴廊"}
    if "quests" not in char_data:
        char_data["quests"] = []
    
    # Check if quest exists, else append
    has_quest = False
    for q in char_data["quests"]:
        if q["quest_name"] == quest_log["quest_name"]:
            has_quest = True
            break
            
    if not has_quest:
        char_data["quests"].append(quest_log)
        char_data["score"] += 1000000
        
        # Consumed soup
        items = char_data.get("items", [])
        for i in items:
            if i["name"] == "向神明許願(料理)":
                items.remove(i)
                break
                
    print(f"\n📜 任務日誌更新：成功觸發隱藏主線【無限的真正遺產】！")
    print(f"   當前進度：尋找第一把邏輯鎖鑰 (0/4)")
    print(f"   目標地點：【絕對零度的冰霜迴廊】")
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"🏆 觸發隱藏主線，獲得積分：1,000,000 分！ (當前總積分：{char_data['score']} 分)")
    print("銀河 的面前出現了一道散發著極寒死氣的冰藍色傳送門。")
    print("是否要跨入【絕對零度的冰霜迴廊】？")

if __name__ == "__main__":
    run()
