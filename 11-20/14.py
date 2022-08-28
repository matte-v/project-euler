"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
import timeit


def get_next(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def main():
    max_chain_len = 0
    solution = None
    for n in range(1, 1_000_000):
        chain_len = 1
        k = n
        while k != 1:
            k = get_next(k)
            chain_len += 1
        if chain_len > max_chain_len:
            max_chain_len = chain_len
            solution = n
            # print(f"{solution} has chain length {max_chain_len}")
    print(f"The solution is {solution}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
