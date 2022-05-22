import os
import shutil

for os_dir in os.walk(os.path.join(os.getcwd(), 'my_project')):
    if 'templates' in os_dir[0]:
        if os_dir[0].split('templates')[1] != '':
            temp_dir = os_dir[0].split('templates')[1].replace('/', '')
            new_dir = os.path.join(os.getcwd(), 'my_project', 'templates', temp_dir)
            new_file = os_dir[2]
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            for file in new_file:
                old_file_path = os.path.join(os_dir[0], file)
                new_file_path = os.path.join(new_dir, file)
                if not os.path.exists(new_file_path):
                    shutil.copyfile(old_file_path, new_file_path)
