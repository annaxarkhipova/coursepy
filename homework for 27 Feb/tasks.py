import os


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


class Coordinate:

     def __init__(self, file):
          self.file = file

     def read(self):
          reading = open(self.file, 'r')
          a = reading.read()
          reading.close()
          return a

     def write(self):
          y = open(self.file, 'w')
          y.write('Yra!')
          y.close()
          return

     def info(self):
          return os.get_terminal_size(self.file)


print(Coordinate('Desktop/py.py'))



def to_title(name):
     name = ' '.join(word[0].upper() + word[1:] for word in name.split())
     return name

name = "nikita ladoshkin evgenyevich"
print(to_title(name))