

def foo(s):
     l = 0
     for i in s:
          l+= 1
     return l


s = 'word'
r = foo(s)
print(r)


l = [2,3,4,5, 6, 7]

def bar(l):
     r = []
     for v in l:
          r.insert(0, v)
     return r

res = bar(l)
print(res)

# При создании объекта должны приниматься значение оси X и значение оси Y.
# Класс должен иметь метод, который возращает число от 1 до 4,
# тем самым показывая, в каком участке находится точка.

# class Coordinate:
#      def __init__(self, x, y):
#           self.x = x
#           self.y = y
#
#
#
#
#
# k = Coordinate()
# print(k)



def count_symbol(new, some):
     count = 0
     for word in new.lower().split():
          if word == some:
               count += 1
               return count

new, some = count_symbol('Hi, Bill, i am home!', 'i')
print(new, some)



def to_title(name):
     name = ' '.join(word[0].upper() + word[1:] for word in name.split())
     return name

name = "nikita ladoshkin evgenyevich"
print(to_title(name))