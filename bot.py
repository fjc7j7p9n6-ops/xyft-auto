import requests
import json
from datetime import datetime

URL = "https://www.3658kj.com/h5/#/lottery?id=10057"

def fetch_data():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(URL, headers=headers, timeout=10)
        html = res.text

        # 简单提取（后续可以升级成API模式）
        data = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "length": len(html),
            "sample": html[:300]
        }

        return data

    except Exception as e:
        return {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "error": str(e)
        }

def save(data):
    try:
        with open("data.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
    except:
        pass

if __name__ == "__main__":
    data = fetch_data()
    save(data)
    print(data)
