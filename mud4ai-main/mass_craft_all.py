import json, os, time, sys

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai_local_save.json"
CHARACTERS = ["無限", "黑河", "試煉", "魔龍", "銀河"]

ITEMS = [
    {
        "name": "幸運手杖",
        "description": "由神明意志具現化的幸運奇蹟之證。被動：因果律強制修正，所有隨機事件必定觸發最幸運結果；主動：『天命掌控』，瞬間扭轉命運之輪。"
    },
    {
        "name": "創世滅龍之劍",
        "description": "融合了創世法則與滅絕龍族概念的究極神兵。對具備『龍』或『神』屬性的目標造成 9,999,999 倍真理傷害，並能斬斷對手的存在維度。"
    },
    {
        "name": "創世神祇衣裝",
        "description": "以創世源代碼編織而成的奇蹟武裝。絕對免疫所有低於當前維度的法則抹殺、即死與屬性削減，並將受到的傷害轉化為穿著者的神性值。"
    }
]

def mass_craft():
    print("\n" + "="*80)
    print("【 MUD4AI 全員神格化：創世級武裝批量鑄造開始 】".center(80))
    print("="*80 + "\n")
    
    if not os.path.exists(LOCAL_SAVE_FILE):
        print("未找到本地存檔文件！")
        return

    with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
        saves = json.load(f)

    for char_name in CHARACTERS:
        if char_name not in saves:
            saves[char_name] = {"score": 0, "items": [], "skills": [], "location": "未知"}
        
        char_data = saves[char_name]
        print(f"🛠️  正在為 【{char_name}】 鑄造究極神兵...", flush=True)
        time.sleep(0.5)
        
        # Add items if they don't exist (avoid duplicates)
        current_names = [item["name"] for item in char_data.get("items", [])]
        for item in ITEMS:
            if item["name"] not in current_names:
                char_data.setdefault("items", []).append(item)
                print(f"  ✨ 獲得道具：【{item['name']}】")
                time.sleep(0.3)
        
        # Set score to epic levels
        char_data["score"] = max(char_data.get("score", 0), 999999999)
        char_data["title"] = "創世神格持有者"
        
        print(f"🎉 【{char_name}】 裝備同步完成！當前積分：{char_data['score']} (神格化成功)\n")
        time.sleep(0.5)

    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)

    print("="*80)
    print("🏆  全員武裝完畢！創世之力已降臨 MUD4AI 世界。".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    mass_craft()
