import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的神級新手冒險：深淵中的野炊與遺跡探索 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    if PLAYER_NAME not in saves:
        print("未找到存檔！")
        return
        
    char_data = saves[PLAYER_NAME]
    
    print(f"📍 {PLAYER_NAME} 在【被撕裂的第十號深淵房間】擊敗殘影後，決定就地紮營，祭出五臟廟。")
    time.sleep(1.5)
    print("\n🍳 【極限料理系統啟動】")
    print("> 銀河 拿出從時空亂流中順手牽羊的奇異食材，開始了前無古人的烹飪！")
    time.sleep(2)
    
    # Dish 1
    print(f"\n🍲 製作料理一：【向神明許願】")
    print(f"   動作：銀河 將一堆未經處理的發光真菌與礦石丟進鍋裡，雙手合十開始祈禱。")
    print(f"   結果：奇蹟發生了！神明似乎聽到了祈求，鍋裡發出刺眼的聖光，所有食材化為一碗熱氣騰騰的黃金高湯！")
    print(f"   ✨ 獲得料理：【向神明許願 (稀有度：傳說)】 - 喝下後 24 小時內，運氣值爆表，走路都會撿到神裝。")
    char_data.setdefault("items", []).append({"name": "向神明許願(料理)", "description": "喝下後運氣爆表的傳說高湯。"})
    time.sleep(2.5)

    # Dish 2
    print(f"\n🥧 製作料理二：【仰望星空派】")
    print(f"   動作：銀河 拿出從迷霧森林抓來的『虛空魔魚』，將牠們的頭部筆直朝上插在麵團裡，送入深淵業火中炙烤。")
    print(f"   結果：出爐時，所有魚頭的死魚眼直直盯著天空，發出詭異的低頻精神波！")
    print(f"   ✨ 獲得料理：【仰望星空派 (稀有度：邪門)】 - 食用後免疫一切精神控制，並對看到這道菜的敵人造成巨額精神污染傷害。")
    char_data.setdefault("items", []).append({"name": "仰望星空派(料理)", "description": "造型驚悚但能免疫精神控制的邪門派。"})
    time.sleep(2.5)

    # Dish 3
    print(f"\n🍚 製作料理三：【墨魚蛋炒飯】")
    print(f"   動作：銀河 利用『極限一擊』的劍氣快速翻炒米飯，並加入『深淵魔王烏賊』的漆黑墨汁。")
    print(f"   結果：整鍋炒飯黑得連光線都能吞噬，但卻散發出讓人靈魂顫抖的極致海鮮香氣！")
    print(f"   ✨ 獲得料理：【墨魚蛋炒飯 (稀有度：史詩)】 - 吃完後全身化為純黑，獲得絕對隱身效果 30 分鐘。")
    char_data.setdefault("items", []).append({"name": "墨魚蛋炒飯(料理)", "description": "能賦予絕對隱身效果的極致美味。"})
    time.sleep(2.5)
    
    char_data["score"] += 150000
    print("\n🎉 廚藝大突破！獲得料理經驗，積分增加 150,000 分！")
    time.sleep(2)
    
    print(f"\n=======================================================================")
    print(f"💍 吃飽喝足後，{PLAYER_NAME} 戴上了剛獲得的【時空跳躍戒指(核心)】，決定去看看這世界的其他角落。")
    print("『空間座標鎖定... 隨機尋找已存在的時空錨點... 跳躍！』")
    time.sleep(2.5)
    
    print("\n📍 系統提示：你進行了空間跳躍！")
    print("📍 系統提示：你降臨在一個異常眼熟的空間...")
    time.sleep(1.5)
    
    print("\n🌪️ 探索區域：【被徹底掠奪的空間 (原深淵第 7 房間)】")
    print("描述：這個房間空無一物，連地磚都被人撬走了。牆上留著一行囂張的刻字：『無限 大人到此一遊，寶藏我全拿走了哈哈哈哈！』")
    time.sleep(2.5)
    
    print("\n「這不就是稍早無限前輩瘋狂掃蕩 10 個房間的遺跡嗎！」銀河 啞然失笑。")
    print("「看來【時空跳躍戒指】帶我回到了因果律的交會點。再跳躍一次看看！」")
    time.sleep(2)
    
    print("\n💍 再次發動【時空跳躍戒指(核心)】！")
    time.sleep(1.5)
    
    print("\n📍 系統提示：你降臨在另一個存在玩家痕跡的區域...")
    print("🔥 探索區域：【焦黑的地下城王座 (原 魔龍 的討伐地)】")
    print("描述：整座地牢被威力極強的魔法陣『六位合一』徹底轟平。王座上只留下一堆灰燼，以及一個牌子：")
    print("『魔龍 參上。這裡的 Boss 太弱了，不堪一擊。』")
    time.sleep(2.5)
    
    char_data["location"] = "焦黑的地下城王座"
    char_data["score"] += 50000
    
    print(f"\n💡 {PLAYER_NAME} 恍然大悟：原來過去的傳奇玩家們（無限、魔龍、黑河、試煉）都在這個世界留下了不可磨滅的物理痕跡！")
    print(f"探勘前人遺跡，積分增加 50,000 分！")
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"📍 {PLAYER_NAME} 當前位置：【{char_data['location']}】")
    print(f"🏆 {PLAYER_NAME} 當前總積分：{char_data['score']} 分")
    print(f"🎒 背包最新物品夾帶了三大傳奇料理！")
    print(f"接下來，銀河要在廢墟中憑弔前輩，還是要繼續踏上新的征程？")

if __name__ == "__main__":
    run()
