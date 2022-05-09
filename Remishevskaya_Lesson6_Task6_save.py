import sys


if len(sys.argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        print(bakery.read())
elif len(sys.argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        for idx, line in enumerate(bakery):
            if idx + 1 >= int(sys.argv[1]):
                print(line.strip())
elif len(sys.argv) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as bakery:
        for idx, line in enumerate(bakery):
            if (idx + 1 >= int(sys.argv[1])) and (idx + 1 <= int(sys.argv[2])):
                print(line.strip())
