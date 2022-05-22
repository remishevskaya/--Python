import os
import json

folder_name = r'/Users/karinaremisevskaya/PycharmProjects/--Python'

dir_size = {}
dir_names = {}

for item in os.listdir(folder_name):
    size = 100
    while os.stat(item).st_size > size:
        size *= 10
    if dir_size.get(size) is None:
        dir_size.setdefault(size, 0)
        dir_size[size] = dir_size[size] + 1
    if dir_names.get(size) is None and os.path.isfile(item):
        dir_names.setdefault(size, list())
        dir_names[size].append(item.split('.')[1])
    else:
        dir_size[size] = dir_size[size] + 1
        if os.path.isfile(item):
            dir_names[size].append(item.split('.')[1])

for key, value in dir_size.items():
    dir_size[key] = (value, dir_names[key])

keys_sort = list(dir_size.keys())
keys_sort.sort()
for key in keys_sort:
    print(f'{key}: {dir_size[key]}')

folder_name = folder_name.split('/')[-1]
file_name = f'{folder_name}_summary.json'

with open(file_name, 'w', encoding='utf-8') as f:
    dir_size_w = json.dumps(dir_size)
    f.write(dir_size_w)