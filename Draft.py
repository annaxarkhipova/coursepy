
'''
Draft
'''

# from random import randint
#
#
# num = str(randint(1000,9999))
# print(num)
# user = input('Введите число: ')
#
#
# cows, bulls = 0, 0
# for i in range(4):
#     if num[i] == user[i]:
#         cows += 1
# print('У вас {} коров и {} быков'.format(cows, bulls))



# draw_board(3)
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---


# num = int(input('Введите число: '))
#
#
# a = '---'
# b = '|'
# if num <= 100:
#     for space in range(num):
#             print((b + '\n' + ' ' + a) + (' ' + b))


# import math
#
# # def graph(foo, b):
# b = [9, 25, 100]
# res = '#'
#
# for i in b:
#     foo = math.sqrt(int(i))
#     if i > 1:
#         pics = res * int(i)
#         print(i,':', pics)

# graph(math.sqrt, [9, 25, 100])



import matplotlib.pyplot as plt

plt.figure(figsize=(7,5))
x = [18, 15, 11, 9, 8, 6]
labels = ['Java', 'C', 'C++', 'PHP', '(Visual) Basic', 'Python']
explode = [0, 0, 0, 0, 0, 0.2]

plt.pie(x, labels = labels, explode=explode, autopct='%1.1f%%', shadow=True);
plt.show()