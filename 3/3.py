"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from commons.numbers import primes


def main():
    sol = max(primes(600851475143))
    print(f'The solution is {sol}')


if __name__ == '__main__':
    main()
