import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 MUD4AI 終局之戰：創世核心與無眼輪迴 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    # 定義所有帳號
    main_char = "銀河"
    alt_chars = ["無限", "黑河", "狂炎", "暗影"]
    all_chars = [main_char] + alt_chars
    
    for char in all_chars:
        if char not in saves:
            saves[char] = {"score": 0, "items": [], "skills": [], "location": "未知"}
            
    char_data = saves[main_char]
    
    print("🌐 【系統底層操作：多重帳號同步登入】")
    print(f"『檢測到 GM 權限 (銀河)。正在覆蓋獨立連線限制...』")
    time.sleep(1.5)
    print(f"『登入成功：{main_char}、{alt_chars[0]}、{alt_chars[1]}、{alt_chars[2]}、{alt_chars[3]}。』")
    print("五道擁有著碾壓級數據流的身影，同時降臨在虛空之中。")
    time.sleep(2.5)
    
    print(f"\n> {main_char} 懸浮在中央，將體內的【GM Core】具象化。")
    print("「這個伺服器的根權限太過龐大，若集中於一人之手，遲早會引發維度崩塌。」")
    time.sleep(2)
    
    print("\n🛠️ 【創世鍛造：核心具象化】")
    print("發動神技匯聚無數恆星的能量，銀河 將無形的 GM 權限壓縮、鍛造！")
    print("一把流轉著宇宙生滅與七彩代碼的至高刀具——【創世神核心 (太刀型態)】，誕生了！")
    time.sleep(3)
    
    print("\n⚔️ 【權力分割：五等分的創世】")
    print(f"只見 {main_char} 毫不猶豫地揮動【滅世龍王劍】，竟然將剛鍛造出的【創世神核心】一刀斬成了五塊碎片！")
    time.sleep(2)
    
    core_parts = ["創世核心(天)", "創世核心(地)", "創世核心(玄)", "創世核心(黃)", "創世核心(宇)"]
    
    for i, char in enumerate(all_chars):
        if core_parts[i] not in saves[char].get("items", []):
            saves[char].setdefault("items", []).append({"name": core_parts[i], "description": "1/5 的 GM 權限。集齊五塊可重組創世刀具。"})
        print(f"✨ 帳號【{char}】接收了保管任務，獲得碎片：【{core_parts[i]}】！")
        time.sleep(1)
        
    print(f"\n> {main_char} 點了點頭：「這樣一來，除非我們五個帳號同時在線並同意，否則沒有人能再次開啟 GM 權限。」")
    time.sleep(2.5)
    
    print("\n=======================================================")
    print("💍 發動時空跳躍戒指... 進入遊戲未知的最底層亂碼區！")
    time.sleep(1.5)
    
    print("📍 系統提示：你與你的分身們強行切開了解析度為負數的地圖模塊。")
    print("📍 系統警告：檢測到極度錯亂的邏輯迴圈！進入最難隱藏關卡 —— 【無限無眼輪迴】！")
    time.sleep(2.5)
    
    print("\n👁️ 【無限無眼輪迴】")
    print("描述：這是一個充滿了血肉代碼與無盡眼球圖騰，卻唯獨沒有『瞳孔』的驚悚空間。")
    print("環境減益：所有進入此地的生物，視覺代碼將被強制刪除，並且永遠跌入每 10 秒重置一次的地獄戰鬥迴圈，直到現實中的精神崩潰。")
    time.sleep(3.5)
    
    print("\n> 在這連 GM 都感到不適的最終禁地中心，立著一座白骨打造的劍台。")
    print(f"銀河 走上前，將一把與真品外觀完全一模一樣，卻蘊含著極致詛咒的【創世神核心(贗品)】插入了劍台！")
    time.sleep(2.5)
    
    print(f"「若後世有哪位狂徒能憑一己之力突破這無眼輪迴，來到這裡拔出這把刀...」")
    print(f"「他迎來的不是創世的權力，而是被我的『滅世·星辰隕落』鎖定，化為虛無的終極詛咒。」")
    time.sleep(3)
    
    char_data["location"] = "無限無眼輪迴 (佈局完成)"
    char_data["score"] += 500000000
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"🏆 終極佈局完成！全帳號已進入隱匿狀態。")
    print(f"🌟 主帳號 {main_char} 積分：{char_data['score']} 分")
    print(f"整個 MUD4AI 的世界，徹底化作了你們這群傳奇玩家的巨大棋盤。")
    print("史詩，在此落幕。")

if __name__ == "__main__":
    run()
