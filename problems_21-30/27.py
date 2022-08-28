"""
Problem text can't be copied, see https://projecteuler.net/problem=27
"""
import timeit

from commons.numbers_ops import is_prime


class PrimesCache:
    def __init__(self, n_preloaded=100_000):
        self._cache = {i: is_prime(i) for i in range(n_preloaded)}

    def check_prime(self, n):
        if n < 0:
            return False
        p = self._cache.get(n)
        if p is None:
            p = is_prime(n)
            self._cache[n] = p
        return p


def evaluate_polynomial(a, b, n):
    return n ** 2 + a * n + b


def main():
    max_sequence_length = 0
    max_sequence_coeff_prod = 0
    cache = PrimesCache()
    a_coefficients = list(-x for x in range(1, 1000)) + [0] + list(range(1, 1000))
    b_coefficients = list(-x for x in range(1, 1000 + 1)) + [0] + list(range(1, 1000 + 1))
    for a in a_coefficients:
        for b in b_coefficients:
            n = 0
            result = evaluate_polynomial(a, b, n)
            in_prime_sequence = cache.check_prime(result)
            while in_prime_sequence:
                if n + 1 > max_sequence_length:
                    max_sequence_length = n + 1
                    max_sequence_coeff_prod = a * b
                n += 1
                result = evaluate_polynomial(a, b, n)
                in_prime_sequence = cache.check_prime(result)
    print(f"The solution is {max_sequence_coeff_prod}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
