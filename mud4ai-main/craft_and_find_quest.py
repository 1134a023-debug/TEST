import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的神級新手冒險：時空與幸運的交匯 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    if PLAYER_NAME not in saves:
        print("未找到存檔！")
        return
        
    char_data = saves[PLAYER_NAME]
    
    print(f"📍 {PLAYER_NAME} 站在【迷霧森林入口】，看著四周散發著微光的古树。")
    time.sleep(1.5)
    print("\n🛠️ 【裝備打造系統觸發】")
    print(f"> {PLAYER_NAME} 撿起了地上的一截充沛著魔力的『古樹靈枝』，並將剛剛獲得的滿溢幸運氣息的『商人餽贈的寶石』鑲嵌其上。")
    time.sleep(2)
    print(f"✨ 發動技能【按部就班】：穩定地引導魔力，保證合成過程零失誤！")
    time.sleep(1.5)
    
    new_weapon = {"name": "幸運手杖", "description": "散發著奇異金光的法杖。只要帶在身上，隨時都會發生不可思議的好事，大幅提升掉寶率與爆擊率！"}
    print(f"🎉 打造成功！獲得全新專屬武器：【{new_weapon['name']}】！")
    print(f"   裝備效果：{new_weapon['description']}")
    
    # 加入背包
    if new_weapon not in char_data.get("items", []):
        char_data.get("items", []).append(new_weapon)
    
    time.sleep(2)
    print(f"\n> 拿著【幸運手杖】的 {PLAYER_NAME}，突然感覺到森林深處傳來一股極不尋常的空間波動。")
    print("「這種波動... 不是普通的怪物，是某個人為撕裂空間留下的痕跡！」")
    time.sleep(2)
    
    print(f"\n🌌 發動主動技能【時空扭曲】！")
    print(f"{PLAYER_NAME} 的眼前出現了一道銀色的空間裂隙，周圍的迷霧瞬間被抽乾。")
    time.sleep(1.5)
    print("你毫不猶豫地踏入了裂隙...")
    time.sleep(1.5)
    
    print("\n📍 系統提示：你跨越了常規地圖，強制降臨隱藏區域 —— 【被撕裂的第十號深淵房間】！")
    char_data["location"] = "被撕裂的第十號深淵房間"
    time.sleep(2)
    
    print("\n🌪️ 【被撕裂的第十號深淵房間】")
    print("描述：這裡根本不存在完整的地面或天空，只有無盡的時空亂流與金色數據碎片。整個空間都殘留著一個名為『無限』的超越者的龐大威壓。")
    time.sleep(2)
    
    print(f"\n🚨 系統警報：你發現了傳說中的史詩級隱藏支線任務！")
    print("在房間的正中央，漂浮著一個由純粹時空法則凝聚而成的殘影分身。分身緩緩睜開了雙眼，發出毫無感情的電子巨響：")
    print("『後來者... 我是 無限 的殘影。想要繼承時空跳躍的遺產，就用你的實力來證明吧。』")
    time.sleep(2.5)
    
    quest_log = {"quest_name": "超限者的試煉", "status": "已接取", "target": "無限的殘影分身"}
    if "quests" not in char_data:
        char_data["quests"] = []
    if quest_log not in char_data["quests"]:
        char_data["quests"].append(quest_log)
        
    print(f"\n📜 任務日誌更新：已自動接取史詩任務【超限者的試煉】！")
    print("   目標：擊敗眼前這尊等級未知的『無限的殘影分身』！")
    print("   危險度：極度致命 (建議組隊或使用超出常理的神技)")
    
    char_data["score"] += 1000
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"📍 {PLAYER_NAME} 當前位置：【{char_data['location']}】")
    print(f"🏆 {PLAYER_NAME} 當前總積分：{char_data['score']} 分")
    print(f"🎒 背包最新物品：【{char_data['items'][-1]['name']}】")
    print(f"⚔️ 史詩戰鬥即將爆發！請下達指令！")

if __name__ == "__main__":
    run()
