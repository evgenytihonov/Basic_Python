from os import path, walk, listdir
import shutil

folder_list = 'my_project'
temp_folder = 'templates'
try:
    for folder, directories, files in walk(folder_list):
        if temp_folder in directories and folder != folder_list:
            for entry in listdir(path.join(folder, temp_folder)):
                shutil.copytree(path.join(folder, temp_folder, entry), path.join(folder_list, temp_folder, path.basename(folder)))

except FileExistsError:
    print(f"Можно работать с {temp_folder}!")