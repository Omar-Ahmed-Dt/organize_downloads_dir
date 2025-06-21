import os
import shutil
from pathlib import Path

# Define your Downloads directory
DOWNLOADS_DIR = str(Path.home() / "Downloads")

# Define categories and their extensions
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

# Reverse lookup for quick category detection
EXT_TO_CATEGORY = {ext: category for category, exts in CATEGORIES.items() for ext in exts}

def organize_downloads(directory: str):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            continue  # Skip existing folders

        _, ext = os.path.splitext(item)
        ext = ext.lower()

        # Determine target category
        category = EXT_TO_CATEGORY.get(ext, "Others")
        target_folder = os.path.join(directory, category)

        # Create category folder if not exists
        os.makedirs(target_folder, exist_ok=True)

        # Move file
        try:
            shutil.move(item_path, os.path.join(target_folder, item))
            print(f"Moved: {item} -> {category}/")
        except Exception as e:
            print(f"Failed to move {item}: {e}")

if __name__ == "__main__":
    organize_downloads(DOWNLOADS_DIR)
