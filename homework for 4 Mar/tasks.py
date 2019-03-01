

import itertools

e = ([1,2,3], [4,5], [6,7])

merged = list(itertools.chain.from_iterable(e))


print(merged)

