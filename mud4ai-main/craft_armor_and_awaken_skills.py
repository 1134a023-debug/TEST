import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的神級晉升：創世武裝與法則覺醒 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    if PLAYER_NAME not in saves:
        print("未找到存檔！")
        return
        
    char_data = saves[PLAYER_NAME]
    
    print(f"📍 {PLAYER_NAME} 握著手中的【邏輯鎖鑰(1)】，感受到其中龐大的基礎數據流。")
    print("「倒懸的時鐘塔... 引力與時間的雙重錯亂，就算是滅世龍王劍，也無法防禦概念級的抹殺。」")
    time.sleep(2)
    
    print(f"\n🛡️ 【神級鑄甲系統啟動】")
    print("銀河 剝落了一絲覆蓋在【邏輯鎖鑰】表面的『絕對零度冰晶』，結合在空間跳躍時收集的『星辰鑌鐵』，以及先前【幸運手杖】牽引來的『神明氣息』。")
    time.sleep(2.5)
    
    print("「將防禦的概念，提升到創世的維度吧！」")
    print("銀河 毫不猶豫地將【粗糙的布衣】丟進了融合光陣中作為概念載體！")
    time.sleep(2)
    
    print("\n✨ 耀眼的燦金光芒照亮了整個冰霜迴廊的廢墟！連系統日誌都出現了短暫的亂碼！")
    time.sleep(1.5)
    
    new_armor = {"name": "創世神祗金裝", "description": "由神明氣息與邏輯代碼編織的絕對防禦。被動：完全免疫任何即死、刪除、扭曲、抹殺類別的法則攻擊，並將所受的任何物理與魔法傷害折射回攻擊者。"}
    print(f"\n🎉 鍛造成功！獲得神話級防具：【{new_armor['name']}】！")
    print(f"   裝備效果：{new_armor['description']}")
    
    # 扣除舊裝備（粗糙的布衣）
    items = char_data.get("items", [])
    for i in items:
        if i["name"] == "粗糙的布衣":
            items.remove(i)
            break
            
    if new_armor not in items:
        items.append(new_armor)
        
    char_data["score"] += 10000000
    time.sleep(2)
    
    print(f"\n🌟 就在【創世神祗金裝】披上 銀河 身軀的瞬間，神裝散發的反哺之力，引發了體內技能的共鳴！")
    print("「力量... 在沸騰？不，是代碼在重組！」")
    time.sleep(2)
    
    print("\n☄️ 【終極技能覺醒】")
    print("系統提示：檢測到玩家持有創世級武裝，基礎技能開始強制突破系統限制！")
    time.sleep(1.5)
    
    # Awakening Skills
    awakened_skills = [
        {"name": "【因果律·絕對命中】", "old": "【按部就班】", "desc": "被動神技：你的任何行動與攻擊都已被寫入因果律的『結果』，無論對手如何閃避或防禦，都將 100% 承受必定命中的打擊。"},
        {"name": "【滅世·星辰隕落】", "old": "【極限一擊】", "desc": "主動神技：揮劍斬裂星河，召喚一顆真實的隕石砸向指定座標，造成不可修復的地形破壞與無視防禦的極巨量 AOE 傷害。"},
        {"name": "【不朽·神性重塑】", "old": "【瞬間恢復】", "desc": "被動/主動神技：生命值歸零時自動觸發，將時間倒流至受傷前一秒並恢復 100% 狀態；主動使用可復活視野內的所有陣亡友軍。"},
        {"name": "【主宰·時空掌控】", "old": "【時空扭曲】", "desc": "主動神技：完全掌控周圍 100 公里內的時間與空間法則，可以隨意加速、暫停、倒退時間，或揉捏空間製造微型黑洞。"}
    ]
    
    old_skills = char_data.get("skills", [])
    char_data["skills"] = [{"name": s["name"], "description": s["desc"]} for s in awakened_skills]
    
    for s in awakened_skills:
        print(f"✨ 技能 {s['old']} 突破極限，覺醒為 👉 {s['name']}！")
        print(f"   效果：{s['desc']}")
        time.sleep(1.5)
        
    char_data["score"] += 40000000
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"🏆 獲得神裝與全技能覺醒，積分暴漲：50,000,000 分！ (當前總積分：{char_data['score']} 分)")
    print("身披【創世神祗金裝】，手持【滅世龍王劍】，裝備著【幸運手杖】與【時空跳躍戒指(核心)】。")
    print("且身懷四大覺醒神技的 銀河，其實力已經完全超越了 MUD4AI 的系統定義。")
    print("「倒懸的時鐘塔... 我來了。」")

if __name__ == "__main__":
    run()
