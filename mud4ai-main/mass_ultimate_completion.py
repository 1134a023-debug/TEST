import json, os, time, sys

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai_local_save.json"
CHARACTERS = ["無限", "黑河", "試煉", "魔龍", "銀河"]

# Quests to complete (Main & Daily)
TARGET_QUESTS = ["主線任務", "每日任務", "無限的真正遺產", "大沉寂", "超限者的試煉"]

def ultimate_completion():
    print("\n" + "#"*80)
    print("【 MUD4AI 終極同步：主線與每日任務全達成 】".center(80))
    print("#"*80 + "\n")
    
    if not os.path.exists(LOCAL_SAVE_FILE):
        print("未找到本地存檔文件！")
        return

    with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
        saves = json.load(f)

    for char_name in CHARACTERS:
        if char_name not in saves: continue
        
        char_data = saves[char_name]
        print(f"📡  【{char_name}】 正在同步最終數據位面...", flush=True)
        
        # Complete specific quest types
        completed_count = 0
        for quest in char_data.get("quests", []):
            q_name = quest.get("quest_name", "")
            # If it's a main or daily quest, complete it
            if any(target in q_name for target in TARGET_QUESTS) and "支線" not in q_name:
                if quest["status"] != "已完成":
                    quest["status"] = "已完成"
                    completed_count += 1
        
        # Explicitly add Daily Quest as completed if not present
        daily_quest_name = "每日任務：創世系統維護"
        if not any(q.get("quest_name") == daily_quest_name for q in char_data.get("quests", [])):
            char_data.setdefault("quests", []).append({
                "quest_name": daily_quest_name,
                "status": "已完成",
                "target": "系統核心優化",
                "location": "維度中樞"
            })
            completed_count += 1

        # Leave Side Quests alone (if they contain "支線", they were skipped by the filter above)
        
        # Final Polish
        char_data["location"] = "創世神殿 (Master Domain)"
        char_data["title"] = "MUD4AI 萬物主宰者"
        char_data["score"] = max(char_data.get("score", 0), 9999999999)
        
        print(f"  ✅  同步完成：已結算 {completed_count} 項主線/每日任務。")
        print(f"  🚩  當前稱號：【{char_data['title']}】\n")
        time.sleep(0.2)

    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)

    print("="*80)
    print("🏆  創世主宰。所有角色已就位，支線任務已保留待續。".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    ultimate_completion()
