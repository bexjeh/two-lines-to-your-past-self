import os

ENTRY = (
    "Don't say yes in the lift on Friday, 14 June, when your boss asks you to cover Saturday.\n"
    "That yes turned into every Saturday, and you missed your daughter's first school play.\n"
)

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
