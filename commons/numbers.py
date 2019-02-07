import math

def all_dividers(n):
    return [x for x in range(1, n+1) if n % x == 0]


def is_prime(n):
    if n in [0, 1, 2]:
        return True
    for x in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def primes(n):
    return [x for x in range(1, math.ceil(math.sqrt(n)) + 1) if n % x == 0 and is_prime(x)]


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def list_mult(a):
    if not a:
        return None
    m = 1
    for x in a:
        m *= x
    return m


def factorization(n):
    if is_prime(n):
        return [n]
    for x in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % x == 0:
            return [x] + factorization(int(n / x))