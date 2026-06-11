import os

def create_test_environment():
    test_dir = os.path.join(os.getcwd(), "test_folder")
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    # Files to create
    files = [
        "photo1.jpg", "photo2.png", "vacation.jpeg",
        "report.pdf", "notes.txt", "data.xlsx",
        "movie.mp4", "intro.mov",
        "song.mp3", "beat.wav",
        "archive.zip", "backup.7z",
        "script.py", "index.html",
        "random_file.unknown"
    ]
    
    for filename in files:
        file_path = os.path.join(test_dir, filename)
        with open(file_path, 'w') as f:
            f.write(f"This is a dummy file for {filename}")
            
    print(f"Test environment created at: {test_dir}")
    print(f"Created {len(files)} test files.")

if __name__ == "__main__":
    create_test_environment()
