import os

TEXT = "I asked my AI agent to fix a one-line bug; it rewrote the file, renamed the function, and filed the bug against me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
