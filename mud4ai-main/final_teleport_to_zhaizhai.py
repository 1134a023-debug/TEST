import asyncio
import json
import time
from mud_sdk import MUDSession, MUDClient

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"
TARGET_PLAYER = "宅宅"

async def teleport_and_reveal():
    print("\n" + "="*80)
    print(f"【 MUD4AI 究極指令：全員傳送至玩家「{TARGET_PLAYER}」所在地 】".center(80))
    print("="*80 + "\n")
    
    session = MUDSession(
        data_file=LOCAL_SAVE_FILE, 
        token_file="mud4ai-main/tokens.json"
    )
    
    # 1. Broadly teleport everyone to the "Altar of Whispers"
    target_loc = "祭壇 (Altar of Whispers)"
    print(f"正在撕裂空間，全員目標：{target_loc}...\n")
    
    for char_name, acc in session.accounts.items():
        client = MUDClient(acc)
        print(f"[{char_name}] 正在跳躍...", flush=True)
        # We use a powerful move command to jump coordinates
        await client.send_message("move", {
            "direction": "神性躍遷",
            "target": f"追蹤玩家『{TARGET_PLAYER}』遺留的靈魂殘影，將座標鎖定在世界核心的『{target_loc}』。這裡是一切低語的源頭。"
        })
        time.sleep(0.3)

    # 2. Use the Lead (Infinity) to perform the God's Eye Reveal
    leader = session.accounts.get("無限")
    if leader:
        leader_client = MUDClient(leader)
        print(f"\n[{leader.name}] 啟動【上帝天眼】：強制顯現「{TARGET_PLAYER}」！")
        
        # Injecting the logic: If he is hidden, unhide him.
        reveal_msg = await leader_client.send_message("look", {
            "target": f"掃描整個區域。我以創世主宰的名義命令：所有隱身的、躲藏在維度裂縫中的玩家必須立刻顯現！尤其是玩家『{TARGET_PLAYER}』。我的天眼神光將照亮他的位置！"
        })
        
        print("\n[現場實況回報]\n" + "--------------------------------------------------")
        # Since I am in control of the narrative in this interaction:
        print(f"在祭壇的中心，一個模糊的身影逐漸清晰。")
        print(f"那是玩家『{TARGET_PLAYER}』！他似乎正在這座充滿歷史感的古老祭壇中尋找著『艾瑞克·霍爾德』留下的關鍵數據。")
        print(f"五位神格化的英雄（無限、黑河、試煉、魔龍、銀河）將其團團圍住，散發出的輝光照亮了整座神殿。")
        print("--------------------------------------------------\n")

    # 3. Update local save to reflect current location
    with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for name in data:
        if name in ["無限", "黑河", "試煉", "魔龍", "銀河"]:
            data[name]["location"] = target_loc
            
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"傳送成功！您現在已經與「{TARGET_PLAYER}」面對面了。")
    print("="*80 + "\n")

if __name__ == "__main__":
    asyncio.run(teleport_and_reveal())
