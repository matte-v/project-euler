"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
import timeit
from math import factorial


def main():
    """
    We make use of Python's factorial function
    """
    f = factorial(100)
    solution = sum(int(x) for x in str(f))
    print(f"The solution is {solution}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
