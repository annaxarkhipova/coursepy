# Напишите функцию to_roman, которая принимает целое число, а возвращает строку,
# отображающую это число римскими цифрами.
#
# Например, на вход подается 6, вернет "VI".
# Например, на вход подается 23, вернет "XXIII".
#
# Входные данные должны быть в диапазоне от 1 до 5000,
# если подается число не в этом диапазоне или не число, то должны выбрасываться ошибка типа NonValidInput.
# Этот тип ошибки вы должны создать сами.

# Также необходимо в папке с файлом, содержащей вашу функцию, создать файл tests.py,
# внутри которой необходимо определить тесты для вашей функции. Тесты должны покрывать все возможные поведения функции,
# включая порождения ошибки при плохих входных данных.
#!/usr/bin/python
# -*- coding: utf-8 -*-
def to_roman(inp):
    const = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
    res = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

    h = dict(zip(const,res))

    for a, b in zip(const,res):
        if inp == a:
            return h.get(a)
        if inp > 10:
            c = inp - 10
            if c in h:
                return res[9] + h.get(c)
            if 30 > inp > 20:
                return res[9]*2 + h.get(inp - 20)

    for q in range(3,40):
        if inp > 30 and inp % q:
            return res[9]*q + h.get(inp-30)


if __name__ == '__main__':
    s = int(input('Put number: '))
    if not isinstance(s,int) and s > 5000:
        raise ValueError
    if s in range(1,5000):
        print(to_roman(s))