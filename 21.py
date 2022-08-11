"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import timeit

from commons.numbers_ops import all_divisors


def d(n):
    divisors = all_divisors(n)
    divisors.remove(n)
    return sum(divisors)


def main():
    amicables = set()
    for n in range(2, 10_000):
        if n not in amicables:
            k = d(n)
            if k != n and n == d(k):
                amicables.add(n)
                amicables.add(k)
    print(f"The solution is {sum(amicables)}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
