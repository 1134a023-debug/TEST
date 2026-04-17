import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的神級冒險：第一把鎖鑰，絕對零度 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    char_data = saves[PLAYER_NAME]
    
    print(f"🚪 {PLAYER_NAME} 毫不猶豫地跨入了散發著死氣的冰藍色傳送門。")
    time.sleep(1.5)
    
    print("\n📍 系統提示：你進入了隱藏極限區域 —— 【絕對零度的冰霜迴廊】！")
    char_data["location"] = "絕對零度的冰霜迴廊"
    time.sleep(1.5)
    
    print("\n❄️ 【絕對零度的冰霜迴廊】")
    print("描述：時間在這裡失去了意義，連空氣中的數據與像素都被凍結成了實體的冰晶。")
    print("環境減益：每秒扣除最大生命值的 10%，並且禁用所有『閃避』與『位移』技能！")
    time.sleep(2.5)
    
    print(f"\n🥶 剛進入迴廊，{PLAYER_NAME} 的血量就開始狂掉：90... 80... 70...")
    print("「好冷... 連代碼都要被凍結了！」")
    time.sleep(2)
    
    print(f"\n🔥 就在危急時刻，背後的【滅世龍王劍】爆發了！")
    print("這把劍是由『魔龍逆鱗』打造，蘊藏著曾經足以焚毀深淵王座的極致火元素。")
    print("劍身自動展開了一道暗紅色的『龍息屏障』，強行將絕對零度逼退了三尺，穩住了 銀河 的生命值！")
    time.sleep(3)
    
    print(f"\n> 藉著屏障的保護，{PLAYER_NAME} 朝著迴廊盡頭走去。在那裡，有一塊散發著奇異代碼光芒的巨大冰柱。")
    print("而在冰柱的正中央，冰封著一把散發著神秘金光的鑰匙。")
    time.sleep(2)
    
    print(f"\n🔍 發動被動技能【按部就班】：銀河 仔細分析了冰塊的結構。")
    print("「這是純粹的『絕對冰結法則』，一般的物理攻擊會直接被吸收。必須用更高階的概念去破壞它！」")
    time.sleep(2.5)
    
    print(f"\n⚔️ {PLAYER_NAME} 高舉【滅世龍王劍】，閉上眼睛，將所有力量灌注於劍刃。")
    print("「主動解放... 『滅世龍吼』！」")
    time.sleep(2)
    
    print("但 銀河 沒有將這股能清空全房間生物體力的能量擴散出去。")
    print("藉助【按部就班】的精密引導，他將整股『龍吼』的爆發力壓縮在了劍尖的一點，並疊加上了【極限一擊】的因果破壞力！")
    time.sleep(3)
    
    print("\n💥 【極限龍吼·單點突破】！")
    print("暗紅色的劍尖點在絕對冰塊上的瞬間，沒有發出任何聲音。")
    print("因為聲音的傳導介質已被瞬間蒸發。緊接著，一圈肉眼可見的空間震波爆開，那塊號稱連時間都能冰封的冰塊，化為了漫天晶瑩的像素碎屑！")
    time.sleep(3)
    
    reward_item = {"name": "邏輯鎖鑰(1)", "description": "由『無限』散落的 GM 權限代碼構成的第一把鑰匙。散發著淡淡的冰霜氣息。"}
    
    print(f"\n🎁 恭喜！成功獲得任務道具：【{reward_item['name']}】！")
    print(f"   物品描述：{reward_item['description']}")
    
    if reward_item not in char_data.get("items", []):
        char_data.get("items", []).append(reward_item)
        
    for q in char_data.get("quests", []):
        if q["quest_name"] == "無限的真正遺產 (連續任務)":
            q["target"] = "尋找第二把邏輯鎖鑰 (1/4)"
            q["location"] = "未知"
            
    char_data["score"] += 15000000 
    
    print(f"\n📜 任務日誌更新：【無限的真正遺產】 (進度 1/4)")
    time.sleep(1.5)
    
    print("\n就在 銀河 握住鑰匙的瞬間，鑰匙內部傳出了一道微弱的座標指引...")
    print("『第二把鎖鑰，沉睡在引力顛倒、邏輯錯亂的【倒懸的時鐘塔】頂端...』")
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"🔑 第一把鑰匙入手！獲得積分：15,000,000 分！ (當前總積分：{char_data['score']} 分)")
    print(f"下一站的目標已經明確：【倒懸的時鐘塔】。")
    print("銀河，準備好迎接顛覆常理的挑戰了嗎？")

if __name__ == "__main__":
    run()
