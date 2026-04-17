import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

TOKEN_FILE = "tokens.json"
SAVE_FILE = "mud4ai_local_save.json"
NEW_CHAR = "銀河"

def setup():
    print(f"正在登出所有舊帳號...")
    
    # 1. Update tokens
    tokens = {}
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, "r", encoding="utf-8") as f:
                tokens = json.load(f)
        except: pass
        
    tokens[NEW_CHAR] = f"offline_token_{NEW_CHAR}_001"
    
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=4, ensure_ascii=False)
        
    # 2. Update local save
    saves = {}
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r", encoding="utf-8") as f:
                saves = json.load(f)
        except: pass
        
    if NEW_CHAR not in saves:
        saves[NEW_CHAR] = {
            "score": 0,
            "items": [{"name": "新手木劍", "description": "一把很普通的木劍。"}, {"name": "粗糙的布衣", "description": "勉強能擋風的衣服。"}]
        }
        
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(saves, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 系統覆寫成功！已為您創建新角色：【{NEW_CHAR}】")
    print(f"================= {NEW_CHAR} 的初始狀態面板 =================")
    print(f"🔹 **等級/稱號**: {NEW_CHAR} (初出茅廬的新手冒險者)")
    print(f"❤️ **血量 (HP)**: 100")
    print(f"🏆 **總積分 (Score)**: 0 分")
    print(f"📍 **當前位置**: 新手村廣場")
    print(f"🎒 **背包神裝 (2 件)**: ")
    print(f"  1. 【新手木劍】 - 一把很普通的木劍。")
    print(f"  2. 【粗糙的布衣】 - 勉強能擋風的衣服。")
    print("=====================================================")

if __name__ == "__main__":
    setup()
