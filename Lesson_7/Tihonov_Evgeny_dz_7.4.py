import os
import django
from collections import defaultdict

def folder_list():
    folder_root = django.__path__[0]
    list_of_files = defaultdict(int)
    for root, dirs, files in os.walk(folder_root):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            list_of_files[size] += 1

    for file_size, file_nums in sorted(list_of_files.items()):
        print(f'размер файлов, до - {file_size}, byte: {file_nums}')

folder_list()