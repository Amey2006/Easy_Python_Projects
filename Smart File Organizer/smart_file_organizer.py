import os
import shutil #Shell utilities

class Organizer:

    def __init__(self,organizing_folder,extention_dict):
        self.folder=organizing_folder
        self.FILE_TYPES=extention_dict

    def get_folder(self,ext):
        for dir,extentions in self.FILE_TYPES.items():
            if ext.lower() in extentions:
                return dir
        
        return "Others"

    def move_to_folder(self,source,destination):
        shutil.move(source,destination)         
   
    def organize(self):
        if self.folder :
            if os.path.exists(self.folder):
                files=os.listdir(self.folder)
                for file in files:
                    full_path = os.path.join(self.folder, file)
                    if os.path.isdir(full_path):
                        continue
                    if os.path.isfile(full_path):
                        name,ext=os.path.splitext(file)
                        its_folder=self.get_folder(ext)
                        target_folder=os.path.join(self.folder,its_folder)
                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)
                            self.move_to_folder(os.path.join(self.folder,file),os.path.join(target_folder,file))
                            print(f"Moved {file} → {its_folder}/")
                        else:
                            self.move_to_folder(os.path.join(self.folder,file),os.path.join(target_folder,file))
                            print(f"Moved {file} → {its_folder}/")


FILE_TYPES = {
    "Images": (".jpg", ".jpeg", ".png", ".gif"),
    "Audio": (".mp3", ".wav"),
    "Videos": (".mp4", ".mkv"),
    "Documents": (".pdf", ".docx", ".txt"),
    "Code": (".py", ".cpp", ".java"),
    "Archives": (".zip", ".rar")
    }
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument(
        "--path",
        required=True,
        help="Folder path to organize"
    )

    args = parser.parse_args()

    organizer = Organizer(args.path, FILE_TYPES)
    organizer.organize()