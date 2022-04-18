def thesaurus(*args):
	"""Создает словарь имен, где ключ - первая буква имени"""
	names_dict = {}
	for name in args:
		names_dict.setdefault(name[0], [])
		names_dict[name[0]].append(name)
	return sorted(names_dict.items())


print(thesaurus('Петр', 'Ольга', 'Сергей', 'Иван', 'Илья'))

