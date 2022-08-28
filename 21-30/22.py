"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import timeit

from commons import read_problem_file


def alpha_value(n):
    return sum(ord(s) - ord('A') + 1 for s in n)


def main():
    names = read_problem_file('p022_names.txt')
    names_list = names.upper().replace('"', '').split(',')
    names_list.sort()
    scores = [(i + 1) * alpha_value(n) for i, n in enumerate(names_list)]
    solution = sum(scores)
    print(f"The solution is {solution}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
