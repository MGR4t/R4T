import threading
import time

from r4t.names import get_rat
from r4t.discovery import (
    find_burrow,
    host_discovery
)

from r4t.chat.server import start_server
from r4t.chat.client import start_client


def main():

    print("""
ᓚᘏᕐᐷ R4T
The Terminal Burrow
""")


    print("🐾 sniffing...")


    ip = find_burrow()


    if not ip:

        print("🕳️ No burrow found")
        print("🐀 Creating one")

        host_discovery()

        threading.Thread(
            target=start_server,
            daemon=True
        ).start()

        time.sleep(1)

        ip = "localhost"

    else:

        print("🧀 Burrow found")


    name = get_rat()

    print(f"You are: 🐀 {name}")

    start_client(ip, name)


if __name__ == "__main__":
    main()