def num_translate_adv(num):
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
    if num == num.capitalize():
        return translate.get(num.lower()).capitalize()
    return translate.get(num)


num = input('Введите число от 1 до 10 на английском: ')
print(num_translate_adv(num))