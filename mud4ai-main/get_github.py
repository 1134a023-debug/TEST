import urllib.request
import json
import sys

def get_commits():
    req = urllib.request.Request(
        'https://api.github.com/repos/chenweichiang/mud4ai/commits',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    try:
        res = urllib.request.urlopen(req)
        commits = json.loads(res.read().decode())[:5]
        for c in commits:
            print(f"{c['commit']['author']['date']} | SHA: {c['sha']}")
            print(f"Message: {c['commit']['message']}\n")
    except Exception as e:
        print("Error fetching commits:", e)

if __name__ == '__main__':
    get_commits()
