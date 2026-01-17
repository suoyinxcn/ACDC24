import os
import time
import requests

URL = os.getenv("TARGET_URL", "https://example.com")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Railway Refresh Bot)"
}

while True:
    try:
        r = requests.get(URL, headers=HEADERS, timeout=15)
        print(f"REFRESH {r.status_code}")
        
        # stop kalau kena rate limit
        if r.status_code == 429:
            print("RATE LIMITED - sleep 5s")
            time.sleep(5)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(3)

    time.sleep(0.3)  # delay kecil biar Railway aman
