import os
import time
import requests

CAMO_URL = os.getenv(
    "CAMO_URL",
    "https://camo.githubusercontent.com/758f27cbbe4be3c2b639357d9acc17d39d78b792b57f745902f0a12aea835dd7/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d786d6f72696e6f7269267374796c653d666f722d7468652d6261646765"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0.0.0 Safari/537.36"
    ),
    "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
    "Referer": "https://github.com/",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}

session = requests.Session()
session.headers.update(HEADERS)

while True:
    try:
        r = session.get(CAMO_URL, timeout=10)
        print("CAMO LOAD:", r.status_code, "bytes:", len(r.content))

        if r.status_code == 429:
            print("RATE LIMIT – sleep 15s")
            time.sleep(15)

    except Exception as e:
        print("ERROR:", e)
        time.sleep(5)

    # delay kecil biar Railway gak kill
    time.sleep(2)
