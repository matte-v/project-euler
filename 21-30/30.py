"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
import timeit


def is_sum_of_fifth_powers_of_digits(n):
    return sum([int(d) ** 5 for d in str(n)]) == n


def main():
    current_sum = 0
    for i in range(2, 10_000_000):  # The max nr with the property is 194979. but how do i know this?
        if is_sum_of_fifth_powers_of_digits(i):
            print(f"Adding {i} to the sum")
            current_sum += i
    print(f"The solution is {current_sum}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
