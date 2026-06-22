import requests
import json
from datetime import datetime

URL = "https://example.com"  # ← 以后你可以改这里

def fetch():
    try:
        r = requests.get(URL, timeout=10)
        html = r.text

        return {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "length": len(html),
            "preview": html[:200]
        }

    except Exception as e:
        return {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "error": str(e)
        }

def save(data):
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            old = json.load(f)
    except:
        old = []

    old.append(data)

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(old, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    data = fetch()
    save(data)
    print("OK:", data)
