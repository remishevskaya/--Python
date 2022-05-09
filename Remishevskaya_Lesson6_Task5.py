import sys
from itertools import zip_longest
sys.argv = input('Задайте имена исходных файлов и выходного файла: ')

with open(sys.argv.split(' ')[0], 'r', encoding='utf-8') as users:
    with open(sys.argv.split(' ')[1], 'r', encoding='utf-8') as hobbies:
        with open(sys.argv.split(' ')[2], 'a+', encoding='utf-8') as users_hobby:
            chunk_size = 8589934592  # 8 гб в байтах
            while True:
                user = users.readlines(chunk_size)
                hobby = hobbies.readlines(chunk_size)
                for user, hobby in zip_longest(user, hobby):
                    if user is None:
                        exit(1)
                    else:
                        users_hobby.write(f'{user.strip()}: {hobby.strip() if hobby is not None else hobby}\n')
                if not hobby:
                    break
