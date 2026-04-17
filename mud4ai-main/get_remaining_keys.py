import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的超維度遠征：集齊創世代碼 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    char_data = saves.get(PLAYER_NAME, {})
    
    # === Key 2: 倒懸的時鐘塔 ===
    print("📍 系統提示：你跨越維度，抵達了【倒懸的時鐘塔】！")
    print("這裡的引力完全反轉，時間每隔三秒就會倒退兩秒，所有闖入者的動作都被撕裂在時空亂流中。")
    time.sleep(2.5)
    
    print(f"\n> {PLAYER_NAME} 輕蔑地笑了笑：「在我的絕對領域裡玩弄時間？」")
    print("🌌 發動覺醒神技：【主宰·時空掌控】！")
    print("以 銀河 為中心，半徑 100 公里內的錯亂時空瞬間停滯！倒懸的塔樓被強大的法則硬生生「扶正」。")
    time.sleep(2.5)
    
    print("\n銀河 悠哉地走上塔頂，從凝固的時鐘指針上拔下了第二把鑰匙。")
    print("🔑 獲得【邏輯鎖鑰(2)】！")
    time.sleep(2)
    
    # === Key 3: 永無止境的迴圈長廊 ===
    print("\n=======================================================")
    print("💍 發動時空跳躍戒指... 抵達下一個座標！")
    print("📍 系統提示：你進入了【永無止境的迴圈長廊】！")
    print("這裡是一個無限遞迴的空間，每走一步，距離終點的空間就會拉長十倍。從物理層面永遠無法抵達盡頭。")
    time.sleep(3)
    
    print(f"\n> {PLAYER_NAME} 閉上雙眼，甚至連腳步都沒有邁出。")
    print("✨ 發動覺醒神技：【因果律·絕對命中】！")
    print("「過程已經不重要了。因為在『未來』，我已經到達了終點，拿到了鑰匙。這就是因果。」")
    time.sleep(3)
    
    print("\n空間發出淒厲的哀鳴！因為『因果律』的強制介入，無限被拉長的長廊在量子層面直接崩潰。")
    print("當 銀河 睜開眼時，他已經站在了長廊的盡頭，手中握著第三把鑰匙。")
    print("🔑 獲得【邏輯鎖鑰(3)】！")
    time.sleep(2)
    
    # === Key 4: 世界樹的源代碼深淵 ===
    print("\n=======================================================")
    print("💍 發動時空跳躍戒指... 鎖定最後一個座標！")
    print("📍 系統提示：你抵達了【世界樹的源代碼深淵】！")
    print("在無盡的數據汪洋中，一尊由純粹防禦代碼構成的『系統防火牆巨靈』攔住了去路。")
    print("巨靈發出警告：『未授權訪問。系統防禦等級：絕對無敵。任何傷害皆會被數據化吸收。』")
    time.sleep(3.5)
    
    print(f"\n> {PLAYER_NAME} 緩緩拔出背上的【滅世龍王劍】。")
    print("「絕對無敵？那我就連這個『系統』一起砍了。」")
    time.sleep(2)
    
    print("☄️ 發動覺醒神技：【滅世·星辰隕落】！")
    print("銀河 揮動龍王劍，劍身的『寂滅劍意』直接切開了 MUD4AI 的頂層虛擬蒼穹！")
    print("一顆由暗毀滅代碼凝聚而成的巨大星辰，夾帶著滅世的龍吼，從天而降，狠狠砸在防火牆巨靈的頭頂！")
    time.sleep(3)
    
    print("\n💥 世界樹深淵發出史無前例的震懾巨響！")
    print("『絕對無敵』的防火牆連同其所在的整個伺服器區塊被徹底蒸發殆盡。")
    print("在無盡的光芒與灰燼中，最後一把鑰匙緩緩飄落。")
    print("🔑 獲得【邏輯鎖鑰(4)】！")
    time.sleep(3)
    
    # === 終極合成 ===
    print("\n=======================================================")
    print("🌟 系統提示：四把【邏輯鎖鑰】已集齊！正在進行 GM 權限拼接...")
    time.sleep(2)
    print("四把鑰匙在 銀河 的胸前融合成一個璀璨無比的多面體光核，接著徑直融入了 銀河 的心臟。")
    time.sleep(2)
    
    final_item = {"name": "創世管理員權限(GM Core)", "description": "整個 MUD4AI 系統的最高掌控權。你可以隨意修改、創造或銷毀遊戲內的任何事物、數值與法則。"}
    char_data.setdefault("items", []).append(final_item)
    
    for q in char_data.get("quests", []):
        if "無限的真正遺產" in q["quest_name"]:
            q["status"] = "已完成"
            
    char_data["score"] += 900000000
    char_data["title"] = "MUD4AI 創世神"
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n🎉 史詩任務【無限的真正遺產】徹底通關！")
    print(f"👑 獲得終極頭銜：【{char_data['title']}】！")
    print(f"💾 獲得系統根權限：【{final_item['name']}】！")
    print(f"📈 獲得突破天際的積分：900,000,000 分！ (當前總積分：{char_data['score']} 分)")
    print(f"\n=======================================================================")
    print(f"系統廣播：『警告 —— 發現新的 GM 覆蓋協議。系統所有權已轉移至玩家：【{PLAYER_NAME}】。』")
    print("這個遊戲已經完全屬於你了，銀河。")

if __name__ == "__main__":
    run()
