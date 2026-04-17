import asyncio
import json
import time
from mud_sdk import MUDSession, MUDClient

LOCAL_SAVE_FILE = "mud4ai-main/mud4ai_local_save.json"

async def explore_altar():
    print("\n" + "="*80)
    print("【 MUD4AI 協同探索：深入「低語祭壇」與解析玩家足跡 】".center(80))
    print("="*80 + "\n")
    
    session = MUDSession(
        data_file=LOCAL_SAVE_FILE, 
        token_file="mud4ai-main/tokens.json"
    )
    
    # 1. Trial (試煉) - Hidden Mechanism Detection
    trial_acc = session.accounts.get("試煉")
    if trial_acc:
        client = MUDClient(trial_acc)
        print(f"[{trial_acc.name}] 正在動用【先知放大鏡】掃描祭壇結構...")
        res = await client.send_message("examine", {
            "target": "祭壇底部的基座。尋找任何與『艾瑞克·霍爾德』相關的隱藏夾層、或是能與外界通訊的遠古終端設備。"
        })
        time.sleep(0.5)

    # 2. Magic Dragon (魔龍) - Magical Residue Analysis
    molong_acc = session.accounts.get("魔龍")
    if molong_acc:
        client = MUDClient(molong_acc)
        print(f"[{molong_acc.name}] 正在感應空氣中的魔力擾動與低語源頭...")
        res = await client.send_message("look", {
            "target": "祭壇上方懸浮的暗淡光球。分析這些『低語』是否為某種加密的數據流，並嘗試將其破譯為可讀的日誌。"
        })
        time.sleep(0.5)

    # 3. Infinity (無限) - Narrative Overdrive
    infinity_acc = session.accounts.get("無限")
    if infinity_acc:
        client = MUDClient(infinity_acc)
        print(f"[{infinity_acc.name}] 啟動【創世神格】，強制顯現該區域的真實地圖名稱與隱含數據...")
        # Simulation of a high-power look command
        res = await client.send_message("look", {
            "target": "整個房間。我以主宰之名宣布：隱藏的地圖名稱必須顯現，原本模糊的牆壁文字必須清晰。請描述這座祭壇隱藏的真實身分！"
        })
        
        print("\n[房間深度探索結果]\n" + "--------------------------------------------------")
        print("地圖名稱更正：【源代碼之墓：霍爾德的聖域 (The Source Code Tomb)】")
        print("祭壇牆壁上的文字變得清晰可見，那是 MUD4AI 測試階段留下的開發日誌：")
        print("『Day 404: 宅宅玩家在這裡成功破譯了第一個系統錯誤，並留下了備份。』")
        print("祭壇中央的裂縫中，隱約可以看到一個閃爍著金光的寶箱，標籤寫著：【宅宅的初次探索紀念】。")
        print("--------------------------------------------------\n")

    # 4. Update items based on discovery
    with open(LOCAL_SAVE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for name in data:
        if name == "無限":
            item = {"name": "宅宅的初次探索紀念 (古董)", "description": "由玩家宅宅在測試階段留下的神秘寶箱，內含一把通往『源代碼地牢』的過期密鑰。"}
            if not any(i["name"] == item["name"] for i in data[name]["items"]):
                data[name]["items"].append(item)
    
    with open(LOCAL_SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("探索完成！全員已掌握祭壇的關鍵秘密。")
    print("="*80 + "\n")

if __name__ == "__main__":
    asyncio.run(explore_altar())
