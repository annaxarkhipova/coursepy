
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


num = int(input('Введите число: '))


a = '---'
b = '|'
if num <= 100:
    for space in range(num):
            print((b + '\n' + ' ' + a) + (' ' + b))

