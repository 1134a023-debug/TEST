import asyncio
from mud_sdk import MUDSession, MUDClient

async def main():
    print("--- MUD SDK Verification ---")
    session = MUDSession(
        data_file="mud4ai-main/mud4ai_local_save.json", 
        token_file="mud4ai-main/tokens.json"
    )
    
    print(f"Loaded {len(session.accounts)} accounts.")
    
    # Initialize a client for 'Infinity' (無限) if it exists
    infinity_acc = next((acc for acc in session.accounts.values() if acc.name == "無限"), None)
    if not infinity_acc:
        # Fallback to first available
        infinity_acc = list(session.accounts.values())[0] if session.accounts else None

    if infinity_acc:
        print(f"Testing client for: {infinity_acc.name}")
        client = MUDClient(infinity_acc)
        result = await client.send_message("check_status", {})
        print(f"Action Result: {result}")
    else:
        print("No accounts found in tokens.json!")

if __name__ == "__main__":
    asyncio.run(main())
