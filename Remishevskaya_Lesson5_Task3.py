import itertools
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Вадим', 'Полина']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) <= len(klasses):
    tutor_gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
else:
    tutor_gen = ((tutor, klass) for tutor, klass in itertools.zip_longest(tutors, klasses, fillvalue='None'))
print(*tutor_gen)
print(type(tutor_gen))
