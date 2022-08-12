import itertools
import math


def all_divisors(n):
    assert n > 0, "n should be > 0"
    if n == 1:
        return [1]
    div = []
    repeated_primes = get_repeated_primes(n)
    for k in range(1, len(repeated_primes)):
        combs = itertools.combinations(repeated_primes, k)
        for c in combs:
            div.append(multiply_list_elements(c))
    return sorted(list(set(div)))


def is_prime(n):
    assert n >= 0, "n must be >= 0"
    if n in [0, 1]:
        return False
    if n == 2:
        return True
    for x in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def get_repeated_primes(n):
    repeated_primes = [1]
    while n != 1:
        factor_found = False
        for x in range(2, math.ceil(n ** .5) + 1):
            if n % x == 0 and is_prime(x):
                repeated_primes.append(x)
                n = n // x
                factor_found = True
                break
        if not factor_found:
            repeated_primes.append(n)  # The current n is prime
            break
    return sorted(repeated_primes)


def primes(n):
    return sorted(list(set(get_repeated_primes(n))))


def get_primes_in_interval(from_incl, to_excl):
    assert from_incl < to_excl, 'from_incl should be < to_excl'
    p = []
    while from_incl < to_excl:
        if is_prime(from_incl):
            p.append(from_incl)
        from_incl += 1
    return p


def get_first_n_primes(n):
    assert n > 0, 'n should be > 0'
    p = []
    k = 2
    while len(p) < n:
        if is_prime(k):
            p.append(k)
        k += 1
    return p


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def multiply_list_elements(a):
    if not a:
        return None
    m = 1
    for x in a:
        m *= x
    return m


def is_pytagorean(a, b, c):
    sides = [a, b, c]
    if min(sides) < 0:
        return False
    hypot = max(sides)
    sides.remove(hypot)
    return sides[0] ** 2 + sides[1] ** 2 == hypot ** 2


def solve_second_grade_equation(c2, c1, c0):
    d = (c1 ** 2 - 4 * c0 * c2) ** .5
    return (-c1 + d) / (2 * c2), (-c1 - d) / (2 * c2)
