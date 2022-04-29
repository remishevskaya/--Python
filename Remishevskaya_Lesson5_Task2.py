def odd_to(num):
    """"Выводит генератор нечетных чисел до заданного числа включительно"""
    for odd_num in range(1, num + 1, 2):
        print(odd_num)


odd_to(15)


