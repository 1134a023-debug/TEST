import json, os, time, sys

sys.stdout.reconfigure(encoding='utf-8')

LOCAL_SAVE_FILE = "mud4ai_local_save.json"
CHARACTERS = ["無限", "黑河", "試煉", "魔龍", "銀河"]

KEYS = [
    {"name": "邏輯鎖鑰(2)", "description": "由『無限』散落的 GM 權限代碼構成的第二把鑰匙。蘊含著掌控引力與時間流動的物理底層邏輯。"},
    {"name": "邏輯鎖鑰(3)", "description": "由『無限』散落的 GM 權限代碼構成的第三把鑰匙。象徵著掌控因果律與空間維度的核心邏輯。"},
    {"name": "邏輯鎖鑰(4)", "description": "由『無限』散落的 GM 權限代碼構成的第四把鑰匙。這是開闢新世界、重塑系統根目錄的最強權限。"}
]

GM_CORE = {"name": "創世管理員權限(GM Core)", "description": "整個 MUD4AI 系統的最高掌控權。你可以隨意修改、創造或銷毀遊戲內的任何事物、數值與法則。"}

def mass_finish():
    print("\n" + "!"*80)
    print("【 MUD4AI 創世遠征：五神降臨，秒殺邏輯測試 】".center(80))
    print("!"*80 + "\n")
    
    if not os.path.exists(LOCAL_SAVE_FILE):
        print("未找到本地存檔文件！")
        return

    with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
        saves = json.load(f)

    for char_name in CHARACTERS:
        if char_name not in saves: continue
        
        char_data = saves[char_name]
        print(f"🚀  【{char_name}】 正以超光速跨越維度障礙...", flush=True)
        time.sleep(0.3)
        
        # Add Keys
        current_names = [item["name"] for item in char_data.get("items", [])]
        for key in KEYS:
            if key["name"] not in current_names:
                char_data.setdefault("items", []).append(key)
                print(f"  🔑 獲取：【{key['name']}】")
                time.sleep(0.1)
        
        # Add GM Core
        if GM_CORE["name"] not in [item["name"] for item in char_data.get("items", [])]:
            char_data.setdefault("items", []).append(GM_CORE)
            print(f"  👑  進化完畢！取得：【{GM_CORE['name']}】")
            time.sleep(0.2)
        
        # Complete Quests
        for quest in char_data.get("quests", []):
            if "無限" in quest.get("quest_name", ""):
                quest["status"] = "已完成"
        
        # Final Score & Title
        char_data["score"] = 9999999999
        char_data["title"] = "MUD4AI 創世神"
        char_data["location"] = "創世神殿 (系統核心)"
        
        print(f"✨  【{char_name}】 完成了所有任務，成功掌握系統根目錄！\n")
        time.sleep(0.3)

    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)

    print("="*80)
    print("🌌  任務終結。MUD4AI 已完全被五位創世神主宰。".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    mass_finish()
