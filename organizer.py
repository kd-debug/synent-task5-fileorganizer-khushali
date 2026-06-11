import os
import shutil
from constants import FILE_CATEGORIES, OTHERS_FOLDER

def get_category(extension):
    """
    Returns the category name based on the file extension.
    """
    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return OTHERS_FOLDER

def organize_folder(target_dir):
    """
    Organizes files in the specified directory into subfolders based on their types.
    Returns a dictionary with stats about organized files.
    """
    if not os.path.exists(target_dir):
        raise ValueError(f"The directory {target_dir} does not exist.")

    stats = {cat: 0 for cat in FILE_CATEGORIES.keys()}
    stats[OTHERS_FOLDER] = 0
    
    # Get all files in the directory (excluding directories themselves)
    files = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]
    
    for filename in files:
        # Skip hidden files
        if filename.startswith('.'):
            continue
            
        file_path = os.path.join(target_dir, filename)
        _, extension = os.path.splitext(filename)
        
        category = get_category(extension)
        category_dir = os.path.join(target_dir, category)
        
        # Create category folder if it doesn't exist
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
            
        # Move the file
        try:
            # Handle potential filename collisions
            dest_path = os.path.join(category_dir, filename)
            if os.path.exists(dest_path):
                # If file exists, append a number to the filename
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(category_dir, f"{name}_{counter}{ext}")):
                    counter += 1
                dest_path = os.path.join(category_dir, f"{name}_{counter}{ext}")
            
            shutil.move(file_path, dest_path)
            stats[category] += 1
        except Exception as e:
            print(f"Error moving {filename}: {e}")
            
    return stats

if __name__ == "__main__":
    # Simple CLI test
    test_path = input("Enter path to organize: ")
    if os.path.isdir(test_path):
        results = organize_folder(test_path)
        print("Organization complete!")
        for cat, count in results.items():
            if count > 0:
                print(f"{cat}: {count} files")
    else:
        print("Invalid path.")
