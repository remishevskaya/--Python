from random import choice, shuffle
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(joke: int) -> str:
    """"Генерирует заданное количество шуток"""
    if repeat == 'Да':
        for joke in range(joke):
            noun = choice(nouns)
            adv = choice(adverbs)
            adj = choice(adjectives)
            print(noun, adv, adj)
    else:
        if joke > len(nouns):
            print('Данное количество шуток без повтора невозможно')
        else:
            shuffle(nouns)
            shuffle(adverbs)
            shuffle(adjectives)
            for joke in range(joke):
                print(nouns[joke], adverbs[joke], adjectives[joke])


joke_num = int(input('Введите количество шуток: '))
repeat = input('Разрешить повторы? (Да / Нет) ')
get_jokes(joke_num)
