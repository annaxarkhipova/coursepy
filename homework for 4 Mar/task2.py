


from itertools import compress


def bar(l):
    p = compress(l, [1, 0, 1, 0, 0, 0])
    return list(p)


l = (['hello', 'i', 'write', 'cool', 'code'])
print(bar(l))





# l = (['hello', 'i', 'write', 'cool', 'code'])
# b = [False]
# for i in l:
#     if len(i) == 5:
#         b = [True]
#         data = list(compress(i, b))
#         print(data)  # ['A', 'C', 'D']