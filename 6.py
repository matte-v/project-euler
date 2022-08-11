"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import timeit
from itertools import combinations


def main():
    # (A + B + C)^2 = A^2 + B^2 + C^2 + 2AB + 2AC + 2BC => (A + B + C)^2 - (A^2 + B^2 + C^2) = - (+ 2AB + 2AC + 2BC)
    comb = combinations(list(range(1, 101)), 2)
    list_to_sum = [2 * c[0] * c[1] for c in comb]
    solution = sum(list_to_sum)
    print(f'The solution is {solution}')


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
