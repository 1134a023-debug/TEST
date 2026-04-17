import asyncio
import json
from mud_sdk import MUDSession, MUDClient

async def search_room():
    session = MUDSession(
        data_file="mud4ai-main/mud4ai_local_save.json", 
        token_file="mud4ai-main/tokens.json"
    )
    
    # Use "試煉" (Trial) as the scout, since they have "先知放大鏡"
    scout_acc = session.accounts.get("試煉")
    if not scout_acc:
        print("未找到試煉的帳號進行偵查！")
        return

    client = MUDClient(scout_acc)
    print(f"[{scout_acc.name}] 正在動用【先知權限】鎖定「宅宅的房間」座標...")
    
    # Inject a search query via the 'examine' action
    result = await client.send_message("examine", {
        "target": "利用【先知放大鏡】與 GM 權限掃描整個創世神殿維度，尋找任何隱藏的入口、維度座標或是被標記為『宅宅的房間』或『秘密工坊』的數據塊。請列出所有可能的隱藏路徑！"
    })
    
    print(f"掃描結果：{result}")

if __name__ == "__main__":
    asyncio.run(search_room())
