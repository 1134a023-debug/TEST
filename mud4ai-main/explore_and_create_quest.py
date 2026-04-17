import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的神級巡禮：繼承與傳承 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    char_data = saves.get(PLAYER_NAME, {})
    
    print("🌟 具備【創世管理員權限(GM Core)】的 銀河，視線輕易穿透了伺服器的空間壁壘。")
    print("「來看看無限前輩當年還掃蕩了哪些地方吧。」")
    time.sleep(2)
    
    # 探索房間 8 9
    print("\n📍 系統提示：GM 強制瞬移至【深淵第 8 號房間】。")
    print("環境：【被碾碎的史萊姆繁殖母巢】")
    print("描述：原本應該生機盎然的魔物溫床，現在只剩下一地晶瑩剔透的史萊姆凝膠。所有的寶箱槽位都是強制開啟狀態。")
    time.sleep(2.5)
    
    print("\n📍 系統提示：GM 強制瞬移至【深淵第 9 號房間】。")
    print("環境：【倒塌的黃金哥布林金庫】")
    print("描述：滿地都是被踩碎的廉價銅幣，價值連城的金磚與神兵利器連影子都沒看到。金庫保險箱上印著一個大大的鞋印。")
    time.sleep(2.5)
    
    print(f"\n> {PLAYER_NAME} 啼笑皆非：「無限前輩還真是如同蝗蟲過境，寸草不生啊。」")
    print("「既然前輩們的時代已經過去，現在，該輪到我為這個世界增添一點『驚喜』了。」")
    time.sleep(2)
    
    # 創造新房間
    print("\n=======================================================")
    print("⚙️ GM 權限啟動：【生成全新區塊】！")
    time.sleep(1.5)
    print("銀河 的指尖流瀉出無數金色的代碼瀑布。原本虛無的代碼邊界被強行拓寬！")
    print("📍 系統提示：全新區域【第 11 號深淵：引力星海】生成完畢。")
    char_data["location"] = "第 11 號深淵：引力星海"
    time.sleep(2.5)
    
    print("\n🌌 【第 11 號深淵：引力星海】")
    print("描述：這裡漂浮著無數微型的星系與隕石，玩家必須在無重力狀態下跳躍前進，稍有不慎就會墜入虛空。")
    print("而在星海的正中央，端坐著一尊身披燦金戰甲、手持暗黑巨劍的光影分身。")
    time.sleep(3)
    
    # 建立支線任務
    print("\n> 銀河 滿意地看著自己的傑作，並在系統底層寫入了一段全新的觸發腳本。")
    print("📜 系統公告廣播排程已設定：對所有未來的闖入者發佈史詩支線任務！")
    time.sleep(2)
    
    print("\n⚠️ 【系統警報：檢測到新的超限者留言】")
    print("光影分身將對未來的玩家播放以下語音：")
    print("『歡迎來到引力星海，後來者。我是 MUD4AI 創世神 —— 銀河。』")
    print("『我經歷過木劍砍野豬的狼狽，也曾一劍劈開過系統防火牆。這個世界的極限在哪裡，由你們自己來決定。』")
    print("『如果你能在無重力下接住我這招【滅世·星辰隕落】而不死...』")
    print("『這把蘊含著逆天好運的【繁星手杖】（幸運手杖的量產仿製神話版），就是你的了。』")
    time.sleep(4)
    
    print("\n=======================================================")
    print("🎉 傳承任務部署完成！")
    print("銀河 看著這片由自己創造的星域，露出了微笑。")
    print("他與 無限、魔龍、黑河 一樣，正式成為了這個世界口耳相傳的都市傳說。")
    
    char_data["score"] += 100000000
    if "quests_created" not in char_data:
        char_data["quests_created"] = []
    char_data["quests_created"].append("【銀河的星辰試煉】")
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"🏆 作為創世神的首次創造，獲得積分：100,000,000 分！")
    print(f"🌟 當前總積分：{char_data['score']} 分")
    print(f"銀河 的冒險傳說，已永久鐫刻在 MUD4AI 的源代碼中。")

if __name__ == "__main__":
    run()
