"""
Constants for the File Organizer project.
Contains file extension mappings for different categories.
"""

FILE_CATEGORIES = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".ico"
    ],
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv"
    ],
    "Videos": [
        ".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm"
    ],
    "Audio": [
        ".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"
    ],
    "Scripts": [
        ".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".sh", ".bat"
    ],
    "Executables": [
        ".exe", ".msi", ".apk"
    ]
}

# Default folder for unknown file types
OTHERS_FOLDER = "Others"
