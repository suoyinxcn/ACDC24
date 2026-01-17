import os
import sys
import json
import asyncio
import platform
import requests
import websockets
from colorama import init, Fore
from keep_alive import keep_alive

init(autoreset=True)

status = "dnd"  # online / dnd / idle
custom_status = ""  # isi kalau mau

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print(f"{Fore.RED}Token tidak ditemukan.")
    sys.exit()

headers = {"Authorization": TOKEN}

# Validate token
r = requests.get("https://canary.discordapp.com/api/v9/users/@me", headers=headers)
if r.status_code != 200:
    print(f"{Fore.RED}Token invalid.")
    sys.exit()

user = r.json()
username = user["username"]
userid = user["id"]

async def heartbeat_loop(ws, interval):
    while True:
        await asyncio.sleep(interval)
        await ws.send(json.dumps({"op": 1, "d": None}))

async def onliner():
    async with websockets.connect(
        "wss://gateway.discord.gg/?v=9&encoding=json",
        max_size=2**20  # 1MB aman
    ) as ws:

        hello = json.loads(await ws.recv())
        interval = hello["d"]["heartbeat_interval"] / 1000

        asyncio.create_task(heartbeat_loop(ws, interval))

        identify = {
            "op": 2,
            "d": {
                "token": TOKEN,
                "intents": 0,
                "properties": {
                    "$os": "Windows",
                    "$browser": "Chrome",
                    "$device": "PC"
                },
                "presence": {
                    "status": status,
                    "afk": False,
                    "activities": [{
                        "type": 4,
                        "state": custom_status,
                        "name": "Custom Status"
                    }]
                }
            }
        }

        await ws.send(json.dumps(identify))

        # keep connection alive
        while True:
            await ws.recv()

async def main():
    os.system("cls" if platform.system() == "Windows" else "clear")
    print(f"{Fore.GREEN}Logged in as {username} ({userid})")
    await onliner()

keep_alive()
asyncio.run(main())
