from organizer import organize_folder
import os

test_path = os.path.join(os.getcwd(), "test_folder")
print(f"Organizing: {test_path}")

try:
    results = organize_folder(test_path)
    print("\nOrganization Summary:")
    for cat, count in results.items():
        if count > 0:
            print(f"- {cat}: {count} files")
            
    # Check if folders were created
    print("\nVerifying folder structure:")
    for cat in results.keys():
        cat_dir = os.path.join(test_path, cat)
        if os.path.exists(cat_dir):
            files = os.listdir(cat_dir)
            print(f"[OK] {cat}: {len(files)} files found inside.")
            
except Exception as e:
    print(f"Error: {e}")
