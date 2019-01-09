from os import listdir
from os.path import isfile, join
from pathlib import Path
import os
import shutil

def main():
    img_path = "C:\\Users\\JayTrairat\\Dropbox"
    target_folder = "C:\\Users\\JayTrairat\\Dropbox\\instagram\\"
    for file_name in listdir(img_path):
        if file_name.endswith(".jpg"):
            folder_name = file_name[:7]
            if not os.path.exists(target_folder + folder_name):
                os.makedirs(target_folder + folder_name)
            shutil.move(os.path.join(img_path, file_name), os.path.join(target_folder + folder_name, file_name))

if __name__ == "__main__":
    main()