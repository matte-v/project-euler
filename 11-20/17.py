"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""
import timeit

numbers_dict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    1000: 'one thousand'
}


def get_two_digits_word(n):
    w = numbers_dict.get(n)
    if not w:
        units = n % 10
        tens = n // 10
        w = numbers_dict[tens * 10] + '-' + numbers_dict[units]
    return w


def get_three_digits_word(n):
    hundreds = n // 100
    tens_units = n % 100
    w = numbers_dict[hundreds] + ' hundred'
    if tens_units > 0:
        w += ' and ' + get_two_digits_word(tens_units)
    return w


def get_word(n):
    w = numbers_dict.get(n)
    if not w:
        assert 20 < n < 1000, 'All one digit numbers and 1000 should be in dictionary'
        if n < 100:
            w = get_two_digits_word(n)
        else:
            w = get_three_digits_word(n)
    return w


def main():
    running_sum = 0
    for i in range(1, 1000 + 1):
        w = get_word(i)
        running_sum += len(w.replace(' ', '').replace('-', ''))
    print(f"The solution is {running_sum}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
