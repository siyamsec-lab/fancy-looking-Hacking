import os
import sys
import time
import random
import string

# ─────────────────────────────────────────────
#  HACKER TERMINAL
# ─────────────────────────────────────────────

GREEN = "\033[92m"
CYAN = "\033[96m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

os.system("cls" if os.name == "nt" else "clear")

print(GREEN + r"""
╔══════════════════════════════════════════════════════╗
║           █ H A C K E R   T E R M I N A L █          ║
║                                                      ║
║              ACCESS SIMULATION v3.0                  ║
╚══════════════════════════════════════════════════════╝
""" + RESET)

time.sleep(1)


def fake_data(length=32):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


steps = [
    "Initializing secure shell",
    "Scanning network nodes",
    "Analyzing encrypted packets",
    "Generating authentication sequence",
    "Decrypting simulation data",
    "Establishing virtual connection",
]

for step in steps:
    print(CYAN + f"[+] {step}..." + RESET)
    time.sleep(random.uniform(0.4, 0.9))


print()

for _ in range(15):
    print(
        GREEN +
        f"[DATA] {fake_data()} "
        f"{random.randint(100, 999)}" +
        RESET
    )
    time.sleep(0.08)


print()

# Progress bar
for percent in range(1, 101):
    bar_length = 20
    filled = int(bar_length * percent / 100)

    bar = "█" * filled + "░" * (bar_length - filled)

    sys.stdout.write(
        f"\r{YELLOW}[!] BYPASSING FIREWALL "
        f"{bar} {percent}%{RESET}"
    )
    sys.stdout.flush()

    time.sleep(0.05)

print()
