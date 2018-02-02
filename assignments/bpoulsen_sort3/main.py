import math
import random
import sys

from counter import Counter
from sort_functions import *


def create_random(n):
    return [random.randrange(0, n) for _ in range(n)]


def create_mostly_sorted(n):
    nums = create_random(n)
    nums.sort()
    nums[0], nums[-1] = nums[-1], nums[0]
    return nums


def format_powers(n):
    return '{:02d}'.format(n)


def format_log(n):
    return '{:05.2f}'.format(math.log2(n) if n != 0 else 0)


def main():
    sys.setrecursionlimit(5000)
    sorts = [
        bubble_sort,
        shaker_sort,
        selection_sort,
        quick_sort,
        modified_quick_sort,
        merge_sort,
        hash_sort,
    ]

    delimiter = '\t'

    headers = delimiter + delimiter.join([sort.__name__.split('_')[0] for sort in sorts]) + '\n'

    mostly_sorted_swaps = headers
    mostly_sorted_compares = headers
    mostly_random_swaps = headers
    mostly_random_compares = headers

    for i in range(3, 13):
        size = 2 ** i
        mostly_random = create_random(size)
        mostly_sorted = create_mostly_sorted(size)

        mostly_sorted_swaps += format_powers(i)
        mostly_sorted_compares += format_powers(i)
        mostly_random_swaps += format_powers(i)
        mostly_random_compares += format_powers(i)

        for sort in sorts:
            mostly_sorted_swaps += delimiter
            mostly_sorted_compares += delimiter
            mostly_random_swaps += delimiter
            mostly_random_compares += delimiter

            mostly_random_counter = Counter()
            mostly_sorted_counter = Counter()
            sort(mostly_random[:], mostly_random_counter)
            sort(mostly_sorted[:], mostly_sorted_counter)

            mostly_sorted_swaps += format_log(mostly_sorted_counter.swaps)
            mostly_sorted_compares += format_log(mostly_sorted_counter.compares)
            mostly_random_swaps += format_log(mostly_random_counter.swaps)
            mostly_random_compares += format_log(mostly_random_counter.compares)

        mostly_sorted_swaps += '\n'
        mostly_sorted_compares += '\n'
        mostly_random_swaps += '\n'
        mostly_random_compares += '\n'

    files = {
        'mostly_sorted_swaps.csv': mostly_sorted_swaps,
        'mostly_sorted_compares.csv': mostly_sorted_compares,
        'mostly_random_swaps.csv': mostly_random_swaps,
        'mostly_random_compares.csv': mostly_random_compares,
    }

    for file in files:
        f = open(file, 'w')
        f.write(files[file])
        f.close()

    print('Random Compares')
    print(mostly_random_compares)
    print()
    print('Random Swaps')
    print(mostly_random_swaps)
    print()
    print('Mostly Sorted Compares')
    print(mostly_sorted_compares)
    print()
    print('Mostly Sorted Swaps')
    print(mostly_sorted_swaps)


if __name__ == '__main__':
    main()
