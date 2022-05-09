from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
        with open('users_hobby.txt', 'a+', encoding='utf-8') as users_hobby:
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
