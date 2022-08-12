"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import itertools
import timeit


def main():
    permutations = itertools.permutations(str(i) for i in range(10))
    permutations_str = [''.join(p) for p in permutations]
    permutations_str.sort()
    print(f"The solution is {permutations_str[1_000_000 - 1]}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
