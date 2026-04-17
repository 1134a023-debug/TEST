import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

quests = [
    {
        "giver": "新手村村長",
        "task": "幫忙整理雜亂的村莊圖書館，不求快，只求穩。",
        "action": "仔細地將每一本書籍歸檔，不遺漏任何一個細節。",
        "skill": "【按部就班】",
        "desc": "被動技能：讓你的行動擁有絕對的穩定性，無視外界干擾，保證每一次行動都能 100% 成功執行基礎效果。"
    },
    {
        "giver": "退役的老劍聖",
        "task": "在瀑布下承受水流衝擊，並在極度疲累中揮出突破極限的一劍。",
        "action": "咬牙堅持，在體力即將耗盡的最後一刻，將所有精氣神凝聚於【新手木劍】之上，猛力劈開了瀑布！",
        "skill": "【極限一擊】",
        "desc": "主動技能：燃燒當前所有體力，對目標造成無視防禦的毀滅性單體傷害。"
    },
    {
        "giver": "生命之樹的精靈",
        "task": "前往危險的幽暗森林深處，採集一朵只在月光下綻放的『月光草』。",
        "action": "小心翼翼地避開怪物，用充滿誠意的心摘下了月光草並交給精靈。",
        "skill": "【瞬間恢復】",
        "desc": "主動技能：引動體內生命力，瞬間將 HP 回復至 100%，冷卻時間短暫。"
    },
    {
        "giver": "神祕的時空旅者",
        "task": "在時空裂縫邊緣，嘗試用肉體感知並捕獲一絲游離的空間法則。",
        "action": "閉上雙眼，不顧時空刃的割裂感，強行將一絲銀色的空間法則融入自己體內！",
        "skill": "【時空扭曲】",
        "desc": "主動技能：短暫改變周圍時間與空間的流速，可用於閃避必殺攻擊或瞬間移動至指定位置。"
    }
]

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的按部就班冒險之旅 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    if PLAYER_NAME not in saves:
        saves[PLAYER_NAME] = {"score": 0, "items": [], "skills": []}
        
    if "skills" not in saves[PLAYER_NAME]:
        saves[PLAYER_NAME]["skills"] = []
        
    for i, q in enumerate(quests, 1):
        print(f"📜 [任務 {i}] 來自 {q['giver']} 的委託：")
        print(f"   目標：{q['task']}")
        time.sleep(1.5)
        print(f"   {PLAYER_NAME} 的行動：{q['action']}")
        time.sleep(1.5)
        print(f"   🎉 任務完成！{q['giver']} 傳授了你一項新技能！")
        print(f"   ✨ 習得技能：{q['skill']} - {q['desc']}\n")
        
        # 加分與存檔
        saves[PLAYER_NAME]["score"] += 150
        skill_entry = {"name": q['skill'], "description": q['desc']}
        if skill_entry not in saves[PLAYER_NAME]["skills"]:
            saves[PLAYER_NAME]["skills"].append(skill_entry)
            
        time.sleep(1)
        
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"=======================================================================")
    print(f"✅ {PLAYER_NAME} 的技能欄已更新！當前技能總數：{len(saves[PLAYER_NAME]['skills'])}")
    print(f"🏆 當前總積分：{saves[PLAYER_NAME]['score']} 分")
    print(f"準備迎接下一場冒險！")

if __name__ == "__main__":
    run()
