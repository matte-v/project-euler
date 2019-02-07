"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from commons.numbers import is_palindrome


def main():
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            p = i*j
            if is_palindrome(p) and p > largest:
                largest = p
    print(f'The solution is {largest}')


if __name__ == '__main__':
    main()