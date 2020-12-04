"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from commons.numbers import is_prime


def main():
    running = 0
    for n in range(2, int(2e6)):
        if is_prime(n):
            running += n
    print(f'The solution is {running}')


if __name__ == '__main__':
    main()
