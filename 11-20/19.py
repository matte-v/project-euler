"""
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""
import timeit
from datetime import date, timedelta


def main():
    """
    We make use of Python's datetime module
    """
    date_start = date(1901, 1, 1)
    date_end = date(2000, 12, 31)
    counter = 0
    while date_start <= date_end:
        if date_start.weekday() == 6 and date_start.day == 1:
            counter += 1
        date_start += timedelta(days=1)
    print(f"The solution is {counter}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
