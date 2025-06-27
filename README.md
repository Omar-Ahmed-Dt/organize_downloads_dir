# 🗂️ organize_downloads_dir

A simple Python script that organizes your **Downloads** folder by automatically sorting files into folders based on file type (images, documents, audio, compressed files, etc.).

## 📦 Features

- Automatically detects and classifies files by extension.
- Creates folders like `Images`, `Documents`, `Compressed`, `Programs`, `Audio`, `Text`, `Excel`, `Others`.
- Moves each file into its respective category.
- Skips existing folders and handles edge cases.
- Easy to customize and extend.

## 🚀 How It Works

This script scans your Downloads directory and matches each file's extension to a predefined category. If a match is found, the file is moved into a corresponding folder. Files with unknown or uncommon extensions go into an `Others` folder.

## 🛠️ Setup

### Requirements

- Python 3.x

### Clone the Repo

```bash
git clone https://github.com/Ahmed-Soli/organize_downloads_dir.git
cd organize_downloads_dir
````

### Run the Script

```bash
python organize_downloads_dir.py --help
```

## 🧩 Categories & Extensions

You can customize the categories and associated file extensions by modifying the `CATEGORIES` dictionary in the script:

```python
CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png"},
    "Documents": {".pdf", ".docx"},
    ...
}
```

## 📂 Example Output

```
Downloads/
│
├── Images/
│   └── photo.jpg
├── Documents/
│   └── resume.pdf
├── Compressed/
│   └── archive.zip
└── Others/
    └── unknown.xyz
```

## 💡 Ideas for Enhancement

* Add support for nested folder scanning.
* Add logging to a file.
* GUI version using Tkinter or PyQt.

## 🧑‍💻 Author

**Ahmed Soliman Mohamed**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
