"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""
import timeit

GRID_SIZE = 20


class Cache:
    """
    Let's use a cache to avoid recomputing nr of path for edges that we already visited
    """
    def __init__(self):
        self._cache = {}
        self.put((0, 0), 1)

    @staticmethod
    def as_key(e):
        return f"{e[0]}-{e[1]}"

    def has(self, e):
        return self.as_key(e) in self._cache

    def put(self, e, n):
        self._cache[self.as_key(e)] = n

    def get(self, e):
        return self._cache[self.as_key(e)]


def parents(e):
    up = (e[0] - 1, e[1])
    left = (e[0], e[1] - 1)
    return [x for x in [up, left] if check_valid_edge(x)]


def check_valid_edge(e):
    return 0 <= e[0] <= GRID_SIZE and 0 <= e[1] <= GRID_SIZE


def number_of_paths_leading_to_edge(e, cache):
    if cache.has(e):
        return cache.get(e)
    else:
        n = sum([number_of_paths_leading_to_edge(x, cache) for x in parents(e)])
        cache.put(e, n)
        return n


def main():
    cache = Cache()
    destination_edge = (GRID_SIZE, GRID_SIZE)
    solution = number_of_paths_leading_to_edge(destination_edge, cache)
    print(f"The solution is {solution}")


if __name__ == '__main__':
    t = timeit.timeit(main, number=1)
    print(f"Execution time: {t:.5f}s")
