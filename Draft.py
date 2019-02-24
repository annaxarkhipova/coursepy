


'''
Draft
'''

class Money:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def penny_count(self):
        return self.x * 100 + self.y

    def __add__(self, other):
        return self.penny_count() + other.penny_count()
        # сложение - penny count 330  и penny count 495

    def __sub__(self, other):
        return self - other



m1 = Money(3, 30)
penny = m1.penny_count()
print('m1 в копейках равен {}'.format(penny))

    def __int__(self):
        return self.m1

print(type(m1))

m2 = Money(4, 95)

m3 = m1 + m2

print('Мы получили {}'.format(m3))
# на экране появится "Мы получили 8руб. 25 коп."


#
# if m1 == m2:
#     print('{} и {} равны'.format(m1, m2)
# elif m1 > m2:
#     print('{} больше чем {}'.format(m1, m2)
# else:
#     print('{} меньше чем {}'.format(m1, m2)
