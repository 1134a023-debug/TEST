import json, urllib.request
import sys

username = "銀河"
password = "Pass123!"
url = "https://mud4ai.interaction.tw/register"
payload = json.dumps({"username": username, "password": password}).encode('utf-8')
headers = {"Content-Type": "application/json"}
req = urllib.request.Request(url, data=payload, headers=headers, method='POST')
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
        token = data.get('token')
        if not token:
            print('No token returned')
            sys.exit(1)
        # Load existing tokens.json
        token_path = "tokens.json"
        try:
            with open(token_path, 'r', encoding='utf-8') as f:
                tokens = json.load(f)
        except FileNotFoundError:
            tokens = {}
        tokens[username] = token
        with open(token_path, 'w', encoding='utf-8') as f:
            json.dump(tokens, f, ensure_ascii=False, indent=2)
        print(f"[銀河] Registration Success! Token: {token}")
except Exception as e:
    print('Registration failed:', e)
    sys.exit(1)
