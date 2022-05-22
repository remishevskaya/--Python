import os

dir_size = {}

for item in os.listdir():
    size = 100
    while os.stat(item).st_size > size:
        size *= 10
    if dir_size.get(size) is None:
        dir_size.setdefault(size, 0)
        dir_size[size] = dir_size[size] + 1
    else:
        dir_size[size] = dir_size[size] + 1

keys_sort = list(dir_size.keys())
keys_sort.sort()
for key in keys_sort:
    print(f'{key} bytes: {dir_size[key]} file(s)')