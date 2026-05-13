import os
import shutil

# Folder to organize (change if needed)
folder_path = "C:/Users/Administrator/Desktop/test_folder"

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt", ".csv", ".xlsx"],
    "Videos": [".mp4", ".mov"],
    "Music": [".mp3", ".wav"]
}

# Go through each file
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                target_folder = os.path.join(folder_path, folder)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} → {folder}")
                break
