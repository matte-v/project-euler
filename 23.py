"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import itertools
import timeit

from commons.numbers_ops import all_divisors


def is_abundant(n):
    divisors = all_divisors(n)
    divisors.remove(n)
    return sum(divisors) > n


def main():
    abundant_numbers = [i for i in range(12, 28123+1) if is_abundant(i)]
    # pairs = combinations of abundant numbers + pairs (N, N) with N abundant
    pairs = list(itertools.combinations(abundant_numbers, 2)) + list(zip(abundant_numbers, abundant_numbers))
    numbers_that_are_sum_of_abuntant = set()
    for p in pairs:
        numbers_that_are_sum_of_abuntant.add(sum(p))
    not_sum_of_abundants = [i for i in range(1, 28123+1) if i not in numbers_that_are_sum_of_abuntant]
    print(f"The solution is {sum(not_sum_of_abundants)}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
