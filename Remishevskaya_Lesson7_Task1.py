import os

main_dir = 'my_project'
list_dir = ['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(main_dir):
    os.mkdir(main_dir)
    for dir_ in list_dir:
        if not os.path.exists(os.path.join(main_dir, dir_)):
            os.mkdir(os.path.join(main_dir, dir_))
