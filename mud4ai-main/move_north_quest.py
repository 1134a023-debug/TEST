import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

PLAYER_NAME = "銀河"
LOCAL_SAVE_FILE = "mud4ai_local_save.json"

def run():
    print(f"\n=================== 【 {PLAYER_NAME} 的神級新手冒險 】 ===================\n", flush=True)
    
    # 讀取存檔
    saves = {}
    if os.path.exists(LOCAL_SAVE_FILE):
        with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
            saves = json.load(f)
            
    if PLAYER_NAME not in saves:
        print("未找到銀河的存檔，請先執行 setup_yinhe.py！")
        return
        
    char_data = saves[PLAYER_NAME]
    
    print(f"> {PLAYER_NAME} 握緊了手中的【新手木劍】，步伐穩健地向『北』方前進...")
    time.sleep(1.5)
    print("\n📍 系統提示：你離開了【新手村廣場】...")
    time.sleep(1)
    print("📍 系統提示：你進入了新的區域 —— 【迷霧森林入口】！")
    time.sleep(1.5)
    
    print("\n🌲 【迷霧森林入口】")
    print("描述：這裡被濃密的霧氣壟罩，能見度極低。四周傳來陣陣令人不安的低吼聲。")
    print("內容物：[求救的旅行商人]、[狂暴的巨型野豬] (等級 15)")
    time.sleep(2)
    
    print(f"\n🚨 觸發隨機事件：【商人的危機】！")
    print("一頭體型龐大、雙眼發紅的『狂暴的巨型野豬』正準備將一名跌倒的旅行商人撞碎！")
    time.sleep(2)
    
    print(f"\n> {PLAYER_NAME} 決定挺身而出，並發動了剛習得的神技！")
    time.sleep(1.5)
    
    print(f"✨ 發動被動技能【按部就班】：{PLAYER_NAME} 瞬間進入絕對冷靜狀態，完美預測了野豬的衝撞軌跡與致命弱點。")
    time.sleep(1.5)
    print(f"🔥 發動主動技能【極限一擊】：{PLAYER_NAME} 燃燒全部體力，手中平凡的【新手木劍】爆發出驚人的劍氣，無視野豬的厚甲，一擊貫穿了牠的心臟！")
    time.sleep(2)
    print("💥 『狂暴的巨型野豬』發出淒厲的慘叫，轟然倒地，化為一陣經驗值光芒！")
    time.sleep(1.5)
    
    print(f"⚠️ 警告：由於發動【極限一擊】，{PLAYER_NAME} 體力透支，HP 降至 1 點！")
    time.sleep(1.5)
    print(f"💚 發動主動技能【瞬間恢復】：生命力在體內湧動，{PLAYER_NAME} 眨眼間將 HP 重新恢復至 100/100 滿狀態，甚至連一滴汗都沒流。")
    time.sleep(2)
    
    print("\n🥺 旅行商人驚魂未定地爬起來：「太、太感謝您了！您明明拿著木劍，卻像劍聖一樣強大！這是我的一點心意，請務必收下！」")
    time.sleep(1.5)
    
    # 給予獎勵
    reward_item = {"name": "迷霧森林通行證", "description": "旅行商人贈予的憑證，似乎能驅散前方森林的霧氣。"}
    reward_score = 500
    
    char_data["score"] += reward_score
    if reward_item not in char_data.get("items", []):
        char_data.get("items", []).append(reward_item)
    
    print(f"\n🎉 任務完成：【商人的危機】")
    print(f"🎁 獲得物品：【{reward_item['name']}】 - {reward_item['description']}")
    print(f"📈 獲得積分：{reward_score} 分")
    
    # 寫回存檔
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)
        
    print(f"\n=======================================================================")
    print(f"📍 {PLAYER_NAME} 當前位置：【迷霧森林入口】")
    print(f"🏆 {PLAYER_NAME} 當前總積分：{char_data['score']} 分")
    print(f"🎒 背包物品總數：{len(char_data.get('items', []))} 件")
    print(f"準備迎接下一場冒險！")

if __name__ == "__main__":
    run()
