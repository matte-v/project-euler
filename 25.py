"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
import timeit


def fibonacci():
    i = 1
    prev = 1
    prev2 = 1
    while True:
        if i < 3:
            yield i, 1
            i += 1
        else:
            curr = prev + prev2
            yield i, curr
            prev2 = prev
            prev = curr
            i += 1


def main():
    for i, n in fibonacci():
        if len(str(n)) >= 1000:
            break
    print(f"The solution is {i}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
