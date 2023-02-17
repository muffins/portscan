#!/usr/bin/env python3


import argparse
import asyncio
import socket

PORT_MAX = 10000


async def scan(host: str, port: int) -> int:
    s = socket.socket()
    s.settimeout(0.1)
    try:
        s.connect((host, port))
    except Exception:
        return 1
    return 0


async def main(host: str) -> None:

    for i in range(1, PORT_MAX):
        ret = await scan(host, i)
        if ret == 0:
            print(f"[+] Open port {host}:{i}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("host")
    args = ap.parse_args()

    asyncio.run(main(args.host))