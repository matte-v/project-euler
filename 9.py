"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import timeit

from commons.numbers_ops import is_pytagorean


def main():
    solution_found = False
    for i in range(1, 1001):
        for j in range(1, 1001):
            k = 1000 - i - j
            if is_pytagorean(i, j, k) and i + j + k == 1000:
                sol = i * j * k
                solution_found = True
                break
        if solution_found:
            break
    if solution_found:
        print(f'i, j, k: {i}, {j}, {k}')
        print(f'The solution is {sol}')


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
