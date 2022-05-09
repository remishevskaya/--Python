import json
from itertools import zip_longest

person = {}

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
        for user, hobby in zip_longest(users, hobbies):
            if user is None:
                exit(1)
            else:
                person[user.strip().replace(',', ' ')] = hobby.strip().replace(',', ', ') \
                                                         if hobby is not None else hobby

with open('person.json', 'w', encoding='utf-8') as f_person:
    json.dump(person, f_person, ensure_ascii=False, indent=2)

with open('person.json', 'r', encoding='utf-8') as f_person:
    print(json.load(f_person))
