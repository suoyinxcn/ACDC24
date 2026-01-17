import os
import time
import requests

PROFILE_URL = os.getenv(
    "GITHUB_PROFILE",
    "https://github.com/1800797"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive"
}

session = requests.Session()
session.headers.update(HEADERS)

while True:
    try:
        r = session.get(PROFILE_URL, timeout=15)
        print("PROFILE:", r.status_code)

        # kalau sukses, "liat" bentar
        if r.status_code == 200:
            time.sleep(2)

        # kalau GitHub nge-limit
        if r.status_code == 429:
            print("RATE LIMIT – tidur 10 detik")
            time.sleep(10)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(5)

    # delay kecil (WAJIB biar Railway aman)
    time.sleep(1.5)
