import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的神兵鑄造：尋找滅世素材 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    if PLAYER_NAME not in saves:
        print("未找到存檔！")
        return
        
    char_data = saves[PLAYER_NAME]
    
    print(f"📍 {PLAYER_NAME} 站在冰藍色傳送門前，搖了搖頭：「那裡面的氣息太過極端，光靠這把木劍和手杖恐怕扛不住。」")
    print("「在面對『無限』的真正遺產之前，我需要一把能夠斬斷維度的武器——【滅世龍王劍】！」")
    time.sleep(2.5)
    
    print(f"\n🔎 {PLAYER_NAME} 轉身看向身處的【焦黑的地下城王座 (原 魔龍 的討伐地)】。")
    print("「前輩『魔龍』曾在這裡施展過『六位合一』的滅世魔法，這裡一定殘留著極致的破壞素材！」")
    time.sleep(2)
    
    print("\n✨ 發動被動技能【按部就班】，銀河 開始在深達數十米的焦黑隕石坑中冷靜地挖掘。")
    print("加上【向神明許願】料理殘餘的逆天好運，他很快在王座的廢墟最深處，摸到了一塊滾燙的黑色晶體。")
    time.sleep(2.5)
    
    print(f"\n🎁 獲得素材：【極致焦黑的魔龍逆鱗】！")
    print("描述：承受了『六位合一』魔法卻毫髮無傷的龍族逆鱗，蘊含著毀天滅地的火元素與霸氣。")
    time.sleep(2)
    
    print(f"\n> 但是，光有物理素材還不夠。{PLAYER_NAME} 需要賦予它『斬斷一切』的概念。")
    print("🔥 銀河 拔出陪伴他已久的【新手木劍】，對著空氣中殘留的空間裂縫，毫無保留地釋放了主動技能——【極限一擊】！")
    time.sleep(2.5)
    
    print("一陣連時間都能劈開的劍光閃過，空間裂縫竟然被『斬』出了一塊固態的碎片！")
    print(f"🎁 獲得素材：【概念碎片：寂滅劍意】！")
    time.sleep(2)
    
    print("\n🛠️ 【終極裝備合成系統觸發】")
    print(f"銀河 將【新手木劍】作為劍骨，【魔龍逆鱗】化作劍刃，並將【寂滅劍意】猛力拍入護手之中！")
    print("左手的高舉著【幸運手杖】，強制將合成成功率從 0.0001% 鎖定在 100%！")
    time.sleep(3)
    
    print("\n一道貫穿深淵天際的暗金色光柱沖天而起！周圍焦黑的磚石瞬間被外洩的劍氣絞成粉末！")
    time.sleep(1.5)
    
    new_weapon = {"name": "滅世龍王劍", "description": "由魔龍逆鱗與空間劍意鍛造的超維度神兵。自帶被動：無視物理與魔法防禦；主動解放：『滅世龍吼』，能直接清空當前房間內所有非 Boss 生物的生命值。"}
    print(f"\n🎉 神兵降世！獲得最終兵器：【{new_weapon['name']}】！")
    print(f"   裝備效果：{new_weapon['description']}")
    
    # 扣除舊裝備（新手木劍）
    items = char_data.get("items", [])
    for i in items:
        if i["name"] == "新手木劍":
            items.remove(i)
            break
            
    # 加新裝備
    if new_weapon not in char_data.get("items", []):
        char_data.get("items", []).append(new_weapon)
        
    char_data["score"] += 5000000
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"🏆 神兵鍛造大成功，獲得積分：5,000,000 分！ (當前總積分：{char_data['score']} 分)")
    print("背上【滅世龍王劍】，左手持【幸運手杖】，銀河 的裝備已經達到了這個遊戲的極限巔峰。")
    print("「現在，可以去會一會那個『絕對零度的冰霜迴廊』了。」")

if __name__ == "__main__":
    run()
