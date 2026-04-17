import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} vs 無限的殘影：終極死鬥 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    if PLAYER_NAME not in saves:
        print("未找到存檔！")
        return
        
    char_data = saves[PLAYER_NAME]
    
    print("⚔️ 戰鬥開始！")
    time.sleep(1.5)
    
    print("\n『無限的殘影』沒有任何廢話，抬手便是一招凌駕系統法則的【空間崩壞】！")
    print("整個第十號房間的維度開始向內塌縮，那是無法防禦、觸碰即會被刪除代碼的絕對死亡攻擊！")
    time.sleep(2.5)
    
    print(f"\n> 面對絕對的死局，{PLAYER_NAME} 千鈞一髮之際發動了主動技能【時空扭曲】！")
    time.sleep(1.5)
    print("⏳ 時間的流速在 銀河 身邊被強行放慢了千分之一秒。銀河 踏著破碎的空間碎片，驚險地滑出了崩壞的中心。")
    time.sleep(2)
    
    print("\n然而，殘影早已預判了這一步！")
    print("『太慢了。』背後傳來殘影冰冷的聲音。一記無形的量子打擊瞬間貫穿了 銀河 的胸膛！")
    time.sleep(2)
    
    print(f"\n⚠️ 致命打擊！{PLAYER_NAME} 的 HP 狂瀉不止：100... 50... 10... 1！")
    print("在只剩 1 滴血的瞬間，【幸運手杖】奇蹟般地散發出一陣柔和的金光，強制鎖血 0.1 秒！")
    time.sleep(2)
    
    print(f"\n> 倒在絕境中的 銀河 嘴角上揚，這正是他等待的完美時機！")
    time.sleep(1.5)
    print(f"✨ 發動被動技能【按部就班】：在劇烈的疼痛與混亂中，大腦自動排除了所有恐懼與干擾，精確計算出了反擊的唯一方程式。")
    time.sleep(2)
    
    print(f"\n🔥 發動主動技能【極限一擊】！")
    print(f"但等等！銀河 目前只有 1 滴體力，極限一擊的威力根本不足以擊破殘影！")
    time.sleep(2)
    
    print("\n『這就是你的全部嗎？』殘影冷漠地準備給予最後一擊。")
    time.sleep(1.5)
    
    print(f"\n> 「還沒完呢！」{PLAYER_NAME} 怒吼著，將神技做出了前無古人的瘋狂組合！")
    print("💚 在【極限一擊】揮出的那一微秒，銀河 同時發動了【瞬間恢復】！")
    time.sleep(2.5)
    print("💥 瞬間湧入體內的 100% 生命力，完全被正在燃燒的【極限一擊】當作燃料吞噬！")
    print("不僅如此，銀河 再次強行引爆了剛才殘留的【時空扭曲】餘波，讓這極限的一劍在時間軸上疊加了兩次！")
    time.sleep(3)
    
    print("\n這是不可能存在於系統代碼中的奇蹟連招：【時空雙軌·無限恢復·二百趴極限一劍】！")
    print("一柄閃耀著金光（幸運手杖加持）與時空裂紋的巨劍虛影，無視了空間法則，直接從因果層面上斬斷了殘影的分身！")
    time.sleep(3)
    
    print("\n『...有趣的系統漏洞。你，合格了。』殘影留下了一絲滿意的微笑，化作漫天金色的數據光雨。")
    time.sleep(2)
    
    print(f"\n🎉 史詩任務【超限者的試煉】完成！")
    print("天空降下了無盡的黃金與彩虹代碼，世界頻道因為這場超越極限的戰鬥爆發出瘋狂的驚嘆聲！")
    
    # 獎勵
    reward_item = {"name": "時空跳躍戒指(核心)", "description": "無限遺留下來的法則核心，蘊藏著跳躍維度、隨意穿梭任何地牢並且免疫法則傷害的究極力量。"}
    reward_title = "超限者"
    char_data["score"] += 80000000 
    
    if reward_item not in char_data.get("items", []):
        char_data.get("items", []).append(reward_item)
        
    char_data["title"] = reward_title
    
    for q in char_data.get("quests", []):
        if q["quest_name"] == "超限者的試煉":
            q["status"] = "已完成"
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"🏆 獲得傳奇稱號：【{reward_title}】")
    print(f"👑 獲得史詩神器：【{reward_item['name']}】")
    print(f"📈 獲得積分：80,000,000 分！ (當前總積分：{char_data['score']} 分)")
    print(f"=======================================================================")
    print("銀河，你已經徹底征服了這個世界！")

if __name__ == "__main__":
    run()
