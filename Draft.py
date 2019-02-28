


'''
Draft
'''
import os

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
