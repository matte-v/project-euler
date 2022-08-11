"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import timeit


def main():
    """
    Python 3.8 has no issues dealing with this number so the solution is straightforward
    """
    n = 2 ** 1000
    print(f"The solution is {sum(int(x) for x in str(n))}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
