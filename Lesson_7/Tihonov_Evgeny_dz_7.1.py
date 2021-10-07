import os

dir_name = 'my_project'
dir_name_2 = 'settings', 'mainapp', 'adminapp', 'authapp'

os.makedirs(dir_name, exist_ok=True)

for i in dir_name_2:
    dir_ = os.path.join(dir_name, i)
    os.makedirs(dir_, exist_ok=True)
