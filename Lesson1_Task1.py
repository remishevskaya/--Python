duration = int(input('Введите продолжительность времени: '))
if duration < 0:
    print('Ошибка')
elif duration // 60 == 0:
    print(f'{duration} сек')
elif duration // 60 > 0 and duration // 3600 == 0:
    print(f'{duration // 60} мин {duration % 60} сек')
elif duration // 3600 > 0 and duration // 86400 == 0:
    print(f'{duration // 3600} час {(duration % 3600) // 60} мин {duration % 60} сек')
else:
    print(f'{duration // 86400} дн {(duration % 86400) // 3600} час {(duration % 3600) // 60} мин {duration % 60} сек')
