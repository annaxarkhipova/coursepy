



# Класс Деньги для работы с денежными суммами.
#
# Один объект должен быть иметь два аттрибута: рубли и копейки.
#
# Объект должен иметь метод, возращающий эквивалент объекта только в копейках в виде целого числа.
#
# На экран объект должен выводится как "x руб. y коп." (есть специальный магический метод, отвечающий за то, как объект выводится на экран).
#
# Реализовать сложение, вычитание и операции сравнения между объектами деньгами (для этого есть специальные магические методы).
#
# На следующем слайде описан пример, как в конечном итоге вы будете оперировать собственным классом Деньги.


class Money:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def penny_count(self):
        return self.x * 100 + self.y

    def __add__(self, other):
        return self.penny_count() + other.penny_count()
        # сложение - penny count 330  и penny count 495

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.y and self.x > other.y

    def __float__(self):
        return self.penny_count()



m1 = Money(3, 30)
penny = m1.penny_count()
print('m1 в копейках равен {}'.format(penny))

###################################################

print(type(m1))

m2 = Money(4, 95)
m3 = m1 + m2

print('Мы получили {}'.format(m3))
# на экране появится "Мы получили 8руб. 25 коп."

if m1 == m2:
    print('{} и {} равны'.format(m1, m2)
elif m1 > m2:
    print('{} больше чем {}'.format(m1, m2)
else:
    print('{} меньше чем {}'.format(m1, m2)
