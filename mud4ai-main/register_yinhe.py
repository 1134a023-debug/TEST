import urllib.request
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 註冊新帳號
username = "yinhe1234"
password = "password123"

print("正在登出所有舊帳號 (將不再使用舊的 Token)...")
print(f"準備註冊新帳號: 銀河 (登入用ID: {username})")

req = urllib.request.Request(
    'https://mud4ai.interaction.tw/register', 
    data=json.dumps({"username": username, "password": password}).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    response = urllib.request.urlopen(req)
    res_data = json.loads(response.read().decode('utf-8'))
    token = res_data.get('token')
    
    print("\n✅ 註冊成功！")
    print(f"角色名稱: 銀河")
    print(f"Token: {token}")
    
    # 儲存到 tokens.json (保留舊的或直接覆寫，這裡用 append 方式)
    tokens = {}
    if os.path.exists("tokens.json"):
        with open("tokens.json", "r", encoding="utf-8") as f:
            tokens = json.load(f)
            
    tokens["銀河"] = token
    
    with open("tokens.json", "w", encoding="utf-8") as f:
        json.dump(tokens, f, indent=4, ensure_ascii=False)
        
    print("\nToken 已安全儲存至 tokens.json 中，接下來所有指令將改用【銀河】！")

except Exception as e:
    print(f"❌ 註冊失敗: {e}")
