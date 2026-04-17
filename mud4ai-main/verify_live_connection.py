import asyncio
import json
import logging
from mud_sdk import MUDSession, MUDClient

# Setup basic logging to see the fallback in action
logging.basicConfig(level=logging.INFO)

async def verify_live():
    print("\n" + "="*80)
    print("【 MUD4AI 真實連線驗證 】".center(80))
    print("="*80 + "\n")
    
    session = MUDSession(
        data_file="mud4ai-main/mud4ai_local_save.json", 
        token_file="mud4ai-main/tokens.json"
    )
    
    # Use Infinity to join and check players
    lead_acc = session.accounts.get("無限")
    if not lead_acc:
        print("未找到帳號！")
        return

    client = MUDClient(lead_acc)
    print(f" sedang menghubungkan {lead_acc.name} ... (Real A2A Call)")
    
    # 1. Join
    join_res = await client.send_message("join", {"player_name": lead_acc.name, "token": lead_acc.token})
    print(f"Join Result: {json.dumps(join_res, ensure_ascii=False, indent=2)}")
    
    # 2. Get Players
    print("\n正在獲取全服在線玩家清單...")
    players_res = await client.send_message("players", {})
    
    # Parse the players from the result
    # In A2A, the result might be in artifacts or it might be raw
    print(f"Players Raw Task: {json.dumps(players_res, ensure_ascii=False, indent=2)}")
    
    print("\n" + "="*80)
    print("【 驗證完畢 】".center(80))
    print("="*80 + "\n")

if __name__ == "__main__":
    asyncio.run(verify_live())
