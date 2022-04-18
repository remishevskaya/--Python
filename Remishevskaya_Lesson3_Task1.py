def num_translate(num):
    """Переводит числительные на английский язык"""
    translate = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять"
    }
    return translate.get(num)


num = input('Введите число от 1 до 10 на английском: ')
print(num_translate(num))
