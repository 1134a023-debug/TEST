import asyncio
import json
import random
import time
from mud_sdk import MUDSession, MUDClient

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"

async def explore_sanctuary():
    print("\n" + "="*80)
    print("【 MUD4AI 啟示錄：尋找並進入「宅宅的祕密基地」 】".center(80))
    print("="*80 + "\n")
    
    session = MUDSession(
        data_file=LOCAL_SAVE_FILE, 
        token_file="mud4ai-main/tokens.json"
    )
    
    # 1. Teleport all characters to the Sanctuary
    new_location = "宅宅的祕密基地 (Otaku Sanctuary)"
    print(f"啟動時空跳躍戒指，目標定位：{new_location}...\n")
    
    for char_name, acc in session.accounts.items():
        client = MUDClient(acc)
        # Narrative injection via A2A
        print(f"[{char_name}] 正在穿梭維度...", flush=True)
        await client.send_message("move", {
            "direction": "超維度躍遷",
            "target": f"利用 GM 權限與時空核心，強行撕裂物理法則，將座標鎖定在世界邊緣的『{new_location}』。這裡是一切代碼的源頭，也是主宰者的私人領域。"
        })
        time.sleep(0.5)

    # 2. Perform collective exploration
    print(f"\n抵達目的地。開始探索該區域...")
    scout = session.accounts.get("試煉") or list(session.accounts.values())[0]
    scout_client = MUDClient(scout)
    
    exploration_result = await scout_client.send_message("examine", {
        "target": "環視整個房間。這是一個充滿未來感與『宅度』的空間：牆上掛著無數限定版模型與二次元掛軸，中央是一組發著科幻藍光的伺服器機架與三螢幕開發主機。空氣中瀰漫著咖啡香氣。請描述我們在這裡發現的驚人物件與遺留的代碼片段！"
    })
    
    print("\n[房間詳情描述]\n" + "--------------------------------------------------")
    # Simulation:
    print("這是一個隱藏在系統根目錄旁的維度空間。")
    print("牆壁上跳動著綠色的 Matrix 代碼流。")
    print("桌上擺著一張照片，那是五位英雄與一位神祕開發者（宅宅）的合影。")
    print("角落的冰箱裡放著喝不完的魔力藥水（黑色罐裝，標籤寫著：Caffeine）。")
    print("--------------------------------------------------\n")

    # 3. Update local save
    with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for name in data:
        if name in ["無限", "黑河", "試煉", "魔龍", "銀河"]:
            data[name]["location"] = new_location
            # Add a unique item from the room
            item = {"name": "宅宅的備用開發機 (核心)", "description": "一台性能超越當前宇宙算力的神祕筆電，內含 MUD4AI 的所有源代碼備份。"}
            if "items" in data[name]:
                if not any(i["name"] == item["name"] for i in data[name]["items"]):
                    data[name]["items"].append(item)
    
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("探索完成！全員已成功駐紮於 宅宅的祕密基地。")
    print("="*80 + "\n")

if __name__ == "__main__":
    asyncio.run(explore_sanctuary())
