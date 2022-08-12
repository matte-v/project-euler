"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""
import timeit


def get_unit_fraction_recurring_part(n):
    """
    I don't want to rely on my PC's numeric precision to find out the recurring cycle, so I divide 1/n "by hand"
    """
    result_sequence = [0]
    remainder_sequence = [1 % n]
    result_remainder_history = [f'res{0}rem{1 % n}']
    while True:
        current_dividend = remainder_sequence[-1] * 10
        current_quotient = current_dividend // n
        current_remainder = current_dividend % n
        qr_key = f'res{current_quotient}rem{current_remainder}'
        if current_remainder == 0:
            return []
        elif qr_key in result_remainder_history:
            rem_start_idx = result_remainder_history.index(qr_key)
            return result_sequence[rem_start_idx:]
        else:
            result_sequence.append(current_quotient)
            remainder_sequence.append(current_remainder)
            result_remainder_history.append(qr_key)


def main():
    longest_recurring_size = 0
    d_longest_recurring = 1
    for d in range(2, 1000):
        recurring_part = get_unit_fraction_recurring_part(d)
        if len(recurring_part) > longest_recurring_size:
            longest_recurring_size = len(recurring_part)
            d_longest_recurring = d
    print(f"The solution is {d_longest_recurring}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
