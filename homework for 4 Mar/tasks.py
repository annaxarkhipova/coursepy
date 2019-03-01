

import itertools

def func(e):
    merged = list(itertools.chain.from_iterable(e))
    return merged

e = ([1,2,3], [4,5], [6,7])
print(func(e))