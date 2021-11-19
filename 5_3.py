# 5.3 - 5.4

'''Задание номер 3'''

from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]


rez = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses, fillvalue=None))
# print(type(rez))
print(*rez, sep='\n') # полный список учеников

# print(next(rez)) # список учеников по отдельности





