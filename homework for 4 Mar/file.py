

# Во втором задании вам необходимо написать консольную утилиту.

# Она должна принимать позиционный аргумент dirpath - это будет директория,
# внутри которой утилита создаст новую папку.

# Название новой папки будет зависеть от указанных опций.

# Если указана опция -y, то в названии присуствует текущий год.
# Если -m, то номер текущего месяца.
# Если -d, то номер текущего дня.
# Опции можно комбинировать, подробности на примере.
# Если папка с заданным названием уже существует,
# то нужно просто выводить предупреждение об этом и больше ничего не делать.

# Если не указано ни одной опции, то утилита должна создать папку с именем 'unknown'.

# Чтобы узнать текущий месяц, день или год,
# нужно прочитать атрибуты объекта, который появится в результате вызова функции
# datetime.now() библиотеки datetime.
# Cпособ создания папки Вам придется найти самим.


import argparse
import os
import datetime

dirpath = '/Users/ana/Desktop/2019-03'
os.makedir(dirpath)
fin = os.path.basename(dirpath)



dt = datetime.date(fin)



parser = argparse.ArgumentParser()
parser.add_argument('-y', '--year', action="store_const", const=dt.year,
                    help="brings out current year")

parser.add_argument('-m', '--month', action="store_const", const=dt.month,
                    help="brings out  current month")

parser.add_argument('-d', '--day', action="store_const", const=dt.day,
                    help="brings out current day")
parser.add_argument('')

args = parser.parse_args()

if args.year:
    print('the name has year')
elif args.month:
    print('the name has month')
elif args.day:
    print('the name has day')
elif os.exists(dirpath):
    print('The file is exists')


