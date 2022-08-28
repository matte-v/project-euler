"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import timeit
from collections import Counter

from commons.numbers_ops import get_repeated_primes


def main():
    # factors = [2, 3, 2, 5, 7, 2, 3, 11, 13, 2, 17, 19]  #solvable with no algorithms
    # ...but let's actually code an algorithm
    factors = Counter({1: 1})
    for i in range(2, 21):
        curr = Counter(get_repeated_primes(i))
        # print(f'i is {i} and its factors are {curr}')
        for k, v in curr.items():
            if k not in factors:
                factors[k] = curr[v]
            if factors[k] < curr[k]:
                factors[k] = curr[k]
        # print(f'factors are {factors}')
        m = 1
        for k, v in factors.items():
            m *= k ** v
    print(f'The solution is {m}')


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
