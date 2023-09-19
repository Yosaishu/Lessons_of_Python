import os
import shutil

source_folder = "C:/Users/iluha/Downloads"
destination_folder = "D:/Archive"

def moving (source_folder, destination_folder):
    files = os.listdir(source_folder)
    for files_in_papka in files:
        source = os.path.join(source_folder, files_in_papka)
        destination = os.path.join(destination_folder, files_in_papka)
        shutil.move(source, destination)
print(f'Файлы перемещены{moving(source_folder, destination_folder)}')

def archiving (destination_folder):
    