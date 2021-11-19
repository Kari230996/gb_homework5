
# 5.1 - 5.2

'''Задание номер 1'''
# def odd_to_15(num):
#     for i in range(1, n+1, 2):
#         yield i
#
# n = int(input())
#
# number = odd_to_15(n)
#
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))
# # ..........
# #   и так далее


'''Задание номер 2'''

n = int(input())

numb = (num for num in range(1, n + 1, 2))

print(next(numb))
# print(next(numb))
# print(next(numb))
# print(next(numb))
# ........
# и так далее



