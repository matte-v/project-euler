"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from commons.numbers import is_prime


def main():
    idx = 0
    n = 1
    while idx != 10001:
        n += 1
        if is_prime(n):
            idx += 1
    print(f'The solution is {n}')


if __name__ == '__main__':
    main()
