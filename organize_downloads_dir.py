import os
import shutil
import json
from pathlib import Path
import argparse

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".ppt", ".pptx", ".odt"},
    "Text": {".txt", ".md", ".rtf"},
    "Excel": {".xls", ".xlsx", ".csv"},
    "Compressed": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"},
    "Programs": {".exe", ".msi", ".deb", ".rpm", ".pkg", ".sh"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"},
    "Video": {".mp4", ".mkv", ".mov", ".avi", ".flv"},
}

EXT_TO_CATEGORY = {ext: cat for cat, exts in CATEGORIES.items() for ext in exts}

# Undo log file name
LOG_FILENAME = ".organizer_log.json"


def organize_directory(directory: str, dry_run: bool = False):
    log = []

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            continue

        _, ext = os.path.splitext(item)
        ext = ext.lower()
        category = EXT_TO_CATEGORY.get(ext, "Others")
        target_folder = os.path.join(directory, category)
        new_path = os.path.join(target_folder, item)

        if dry_run:
            print(f"[Dry Run] Would move: {item_path} -> {new_path}")
        else:
            os.makedirs(target_folder, exist_ok=True)
            try:
                shutil.move(item_path, new_path)
                log.append({"from": item_path, "to": new_path})
                print(f"Moved: {item} -> {category}/")
            except Exception as e:
                print(f"Failed to move {item}: {e}")

    if not dry_run and log:
        log_path = os.path.join(directory, LOG_FILENAME)
        with open(log_path, "w") as f:
            json.dump(log, f, indent=2)

        script_name = os.path.basename(__file__)
        print("\n✅ Done organizing files.")
        print(f"ℹ️  To undo, run: python {script_name} --undo --dir {directory}")


def undo_last_operation(directory: str):
    log_path = os.path.join(directory, LOG_FILENAME)
    if not os.path.isfile(log_path):
        print("⚠️  No undo log found in this directory.")
        return

    with open(log_path, "r") as f:
        log = json.load(f)

    for entry in reversed(log):
        src = entry["to"]
        dst = entry["from"]
        try:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
            print(f"Restored: {os.path.basename(src)}")
        except Exception as e:
            print(f"Failed to restore {src}: {e}")

    os.remove(log_path)
    print("✅ Undo complete. Log removed.")


def main():
    parser = argparse.ArgumentParser(
        description="Organize files by type."
    )
    parser.add_argument(
        "--dir", type=str, default=".", help="Directory to organize (default: current directory)"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Simulate file organization without moving anything"
    )
    parser.add_argument(
        "--undo", action="store_true", help="Undo the last organization operation"
    )

    args = parser.parse_args()
    target_dir = os.path.abspath(os.path.expanduser(args.dir))

    if args.undo:
        undo_last_operation(target_dir)
    else:
        organize_directory(target_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
