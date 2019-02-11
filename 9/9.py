"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
from commons.numbers import is_pytagorean


def main():
    for i in range(1, 1001):
        for j in range(1, 1001):
            k = 1000 - i - j
            if is_pytagorean(i, j, k) and i + j + k == 1000:
                sol = i*j*k
                quit(f'The solution is {sol} (i, j, k: {i}, {j}, {k})')


if __name__ == '__main__':
    main()
