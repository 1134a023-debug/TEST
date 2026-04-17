import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# The server requires username length 3-24. We use alphanumeric to be safe,
# and we will use the display name in the game client.
accounts_to_create = {
    "無限大人": "master123", # length 4
    "heihe_bot": "minion123",
    "shilian_bot": "minion123",
    "molong_bot": "minion123"
}

tokens = {}

for user, pwd in accounts_to_create.items():
    req = urllib.request.Request(
        'https://mud4ai.interaction.tw/register', 
        data=json.dumps({"username": user, "password": pwd}).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        response = urllib.request.urlopen(req)
        res_data = json.loads(response.read().decode('utf-8'))
        token = res_data.get('token')
        tokens[user] = token
        print(f"[{user}] Registration Success! Token: {token}")
    except Exception as e:
        print(f"[{user}] Failed: {e}")

# Save tokens to a file for later use
with open("tokens.json", "w", encoding="utf-8") as f:
    json.dump(tokens, f, indent=4, ensure_ascii=False)

print("\nSaved to tokens.json")
