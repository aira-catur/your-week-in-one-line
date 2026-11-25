import os
from pathlib import Path

WEEK_LINE_FINAL = "I meal-prepped five lunches Monday; Friday, I ate the fifth for breakfast at the fridge at 2 a.m."


def emit_line():
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / "entry.txt"
    target_file.write_text(WEEK_LINE_FINAL, encoding="utf-8")


if __name__ == "__main__":
    emit_line()
