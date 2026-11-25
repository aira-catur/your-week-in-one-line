import os

TEXT = (
    "I meal-prepped five lunches Monday; "
    "Friday, I ate the fifth for breakfast at the fridge at 2 a.m."
)


def write_entry(out_dir, text):
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    write_entry(out_dir, TEXT)


if __name__ == "__main__":
    main()
