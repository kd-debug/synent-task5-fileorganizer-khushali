# TidyFiles - Smart File Organizer

TidyFiles is a modern, automated desktop application designed to declutter your folders by intelligently sorting files into categorized subfolders. Built as part of a Python development internship, it focuses on efficiency, a clean UI, and robust file-handling logic.

## 🚀 Features

- **Automated Sorting**: Instantly categorizes files into Images, Documents, Videos, Audio, Archives, Scripts, and more.
- **Modern GUI**: A user-friendly desktop interface built with Tkinter.
- **Smart Conflict Handling**: Automatically renames files if a duplicate exists in the destination folder to prevent data loss.
- **Dynamic Folder Creation**: Only creates folders for categories that actually have files present.
- **Lightweight & Fast**: Uses standard Python libraries (`os`, `shutil`) for maximum compatibility and performance.

## 📂 Project Structure

```text
FileO/
├── app.py                # Main GUI application
├── organizer.py          # Core organization logic
├── constants.py          # File extension mappings
├── create_test_files.py  # Utility to generate test data
├── verify_logic.py       # Script to verify sorting logic
├── run_app.bat           # Windows shortcut to launch app
└── setup_test.bat        # Windows shortcut to setup test files
```

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.x installed on your system.

### How to Run

1. **Clone/Navigate to the project**:
   ```bash
   cd FileO
   ```

2. **Run via Shortcut (Windows)**:
   - Double-click `run_app.bat` to launch the application immediately.
   - Double-click `setup_test.bat` to create a `test_folder` with dummy files for testing.

3. **Run via Terminal**:
   ```powershell
   py app.py
   ```

## 🧠 How it Works

1. **Selection**: User selects a target directory via the folder browser.
2. **Scanning**: The app scans all files in the directory (ignoring hidden files and existing folders).
3. **Classification**: Each file is classified based on its extension using the mappings in `constants.py`.
4. **Relocation**: Files are moved to their respective category folders. If a filename collision occurs, a counter is appended (e.g., `file_1.png`).

## 🛡️ Ethics & Integrity
This project was developed from scratch for internship requirements. All logic and UI designs are original to ensure compliance with strict anti-plagiarism policies.

---
Developed as part of the Python Development Internship Task 1.
