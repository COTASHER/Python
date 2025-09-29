"""
for x1 in range(5):
    for x2 in range(5):
        for x3 in range(5):
            for x4 in range(5):
                print(x1,x2,x3,x4)
"""

"""
from itertools import product
for x in product(range(5), repeat=4):
    print(x)
"""

from itertools import permutations
for p in permutations('ABC', 2):
    print(p)
