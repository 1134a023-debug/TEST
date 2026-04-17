import json

LOCAL_SAVE_FILE = "mud4ai_local_save.json"
REFLECTION_FILE = "MUD4AI_Epic_Finale_Reflection_Detailed.md"
CHARACTERS = ["無限", "黑河", "試煉", "魔龍", "銀河"]

with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
    saves = json.load(f)

status_output = "\n\n---\n\n## 📊 創世神格：最終狀態面板同步\n\n以下為五位創世神在「創世神殿」集結時的最新系統狀態：\n\n```text\n"

for char in CHARACTERS:
    data = saves.get(char, {})
    status_output += f"================= {char} 的終極狀態面板 =================\n"
    status_output += f"🔹 等級/稱號: {data.get('title', char + ' (MUD4AI 傳奇玩家)')}\n"
    status_output += f"❤️ 血量 (HP): 100\n"
    status_output += f"🏆 總積分 (Score): {data.get('score', 0)} 分 (Client-Side 同步)\n"
    status_output += f"📍 當前位置: {data.get('location', '未知')}\n"
    status_output += f"🎒 背包神裝 ({len(data.get('items', []))} 件):\n"
    for i, item in enumerate(data.get('items', []), 1):
        status_output += f"  {i}. 【{item['name']}】 - {item['description']}\n"
    status_output += "=====================================================\n\n"

status_output += "```\n"

with open(REFLECTION_FILE, "a", encoding="utf-8") as f:
    f.write(status_output)

print("Status panels appended successfully.")
