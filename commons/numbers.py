import math


def all_dividers(n):
    return [x for x in range(1, n+1) if n % x == 0]


def is_prime(n):
    for x in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def primes(n):
    return [x for x in range(1, math.ceil(math.sqrt(n)) + 1) if n % x == 0 and is_prime(x)]
