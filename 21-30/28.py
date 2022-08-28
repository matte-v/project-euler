"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""
import timeit


# def generate_ring_capacities(spiral_size):
#     """
#     I call a ring a layer/leap of the spiral, e.g. for a 5x5 spiral the 1st ring is just the cell containing 1,
#     the 2nd ring is composed by the cells containing from 2 to 9,
#     the 3rd ring is composed by the cells containing from 10 to 25.
#     The capacities of these 3 rings are 1, 8 ,16
#     """
#     square_sizes = [1]
#     ring_capacities = [1]
#     while sum(square_sizes) < spiral_size:
#         ss = square_sizes[-1] + 2
#         square_sizes.append(ss)
#         ring_capacities.append((ss - 2) * 4 + 4)
#     return ring_capacities


def generate_rings_max_numbers(n_rings):
    """
    I call a ring a layer/leap of the spiral, e.g. for a 5x5 spiral the 1st ring is just the cell containing 1,
    the 2nd ring is composed by the cells containing from 2 to 9,
    the 3rd ring is composed by the cells containing from 10 to 25.
    The max numbers of these 3 rings are 1, 9, 25
    """
    return [(2 * i + 1)**2 for i in range(n_rings)]


def generate_indexes_of_diagonal_cells(n_rings):
    """
    This can be obtained by drawing some rings of a spiral. Rings and elements in the ring must be zero-indexed
    """
    diag_indexes = [[0]]
    for ring_index in range(1, n_rings):
        list_1 = [1, 3, 5, 7]
        list_2 = [(ring_index - 1) * x for x in [2, 4, 6, 8]]
        element_wise_sum_list = [sum(x) for x in zip(list_1, list_2)]
        diag_indexes.append(element_wise_sum_list)
    return diag_indexes


def main():
    SPIRAL_SIZE = 1001
    n_rings = SPIRAL_SIZE // 2 + 1
    running_sum = 0
    current_n = 1
    rings_max_numbers = generate_rings_max_numbers(n_rings)
    idx_diagonals = generate_indexes_of_diagonal_cells(n_rings)
    for ring_idx, ring_max_nr in enumerate(rings_max_numbers):
        idx_in_ring = 0
        indexes_in_diagonal = idx_diagonals[ring_idx]
        while current_n <= rings_max_numbers[ring_idx]:
            if idx_in_ring in indexes_in_diagonal:
                running_sum += current_n
                # print(f"Adding {current_n} to the current sum")
            idx_in_ring += 1
            current_n += 1
    print(f"The solution is {running_sum}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
