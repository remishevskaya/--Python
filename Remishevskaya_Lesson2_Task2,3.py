some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for idx, word in enumerate(some_list):
    if word.isdigit():
        if int(word) // 10 == 0:
            word = '0' + word
        some_list[idx] = f'"{word}"'
    elif word.startswith('+'):
        if int(word[1:]) // 10 == 0:
            word = word[:1] + '0' + word[1:]
        some_list[idx] = f'"{word}"'
print(' '.join(some_list))
# В задании указано, что вещественные числа мы не трогаем, а в примере в кавычках выведено и +5.
# Я сделала вместе с ними как в примере
