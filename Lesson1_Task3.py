def transform_str(number: int) -> str:
    if 11 <= number <= 19:
        return f'{number} процентов'
    elif number % 10 == 1:
        return f'{number} процент'
    elif 2 <= number % 10 <= 4:
        return f'{number} процента'
    else:
        return f'{number} процентов'


for n in range(1, 101):
    print(transform_str(n))
