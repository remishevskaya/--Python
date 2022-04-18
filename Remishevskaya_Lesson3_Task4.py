def thesaurus_adv(*args) -> dict:
    """Создает словарь имен и фамилий"""
    surnames_dict = {}
    for name in sorted(args):
        surnames_dict.setdefault(name.split(' ')[-1][0], dict())
        if surnames_dict[name.split(' ')[-1][0]].get(name[0]) is None:
            surnames_dict[name.split(' ')[-1][0]][name[0]] = []
        surnames_dict[name.split(' ')[-1][0]][name[0]].append(name)
    keys_sort = list(surnames_dict.keys())
    keys_sort.sort()
    for key in keys_sort:
        print(key, ':', surnames_dict[key])


thesaurus_adv('Иван Иванов', 'Петр Иванов', 'Светлана Петрова', 'Петр Алексеев', 'Марина Алексеева', 'Павел Алексеев')

