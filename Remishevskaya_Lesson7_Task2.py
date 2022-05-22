import linecache
import os

file_str = {}

with open('config.yml', 'r', encoding='utf-8') as conf:
    for idx, line in enumerate(conf):
        if len(line.split(' ')[0]) == 1:
            file_str.setdefault(line.strip().split(' ')[1], {})

        if len(line.split(' ')[0]) == 3:
            num = int(line.split(' ')[0][0]) - 1
            key1 = list(enumerate(file_str.keys()))[num][1]
            if len(line.strip().split(' ')[1:]) == 1:
                file_str[key1][line.strip().split(' ')[1]] = {}
            else:
                file_str[key1]['files'] = line.strip().split(' ')[1:]

        if len(line.split(' ')[0]) == 5:
            num = int(line.split(' ')[0][0]) - 1
            key1 = list(enumerate(file_str.keys()))[num][1]
            key2 = linecache.getline('config.yml', idx).strip().split(' ')[1]
            file_str[key1][key2] = {line.strip().split(' ')[1]: {}}

        if len(line.split(' ')[0]) == 7:
            num = int(line.split(' ')[0][0]) - 1
            key1 = list(enumerate(file_str.keys()))[num][1]
            key2 = linecache.getline('config.yml', idx-1).strip().split(' ')[1]
            key3 = linecache.getline('config.yml', idx).strip().split(' ')[1]
            file_str[key1][key2][key3]['files'] = line.strip().split(' ')[1:]

        if not line.split(' ')[0][0].isdigit():
            start_dir = line.strip()
            if not os.path.exists(start_dir):
                os.mkdir(start_dir)
    for key in file_str.keys():
        for key1 in file_str[key].keys():
            if key1 == 'files':
                if not os.path.exists(os.path.join(start_dir, key)):
                    os.makedirs(os.path.join(start_dir, key))
                    for value1 in file_str[key][key1]:
                        file = os.path.join(start_dir, key, value1.replace(',', ''))
                        open(file, 'w')
            else:
                for key2 in file_str[key][key1].keys():
                    for key3 in file_str[key][key1][key2].keys():
                        if key3 == 'files':
                            new_dir = os.path.join(start_dir, key, key1, key2)
                            if not os.path.exists(new_dir):
                                os.makedirs(new_dir)
                            for value1 in file_str[key][key1][key2][key3]:
                                file = os.path.join(new_dir, value1.replace(',', ''))
                                open(file, 'w')
