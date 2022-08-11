"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import timeit

from commons.numbers_ops import is_prime, get_first_n_primes


def main():
    n = get_first_n_primes(10001)[-1]
    print(f'The solution is {n}')


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
