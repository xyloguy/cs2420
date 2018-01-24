"""
Sorting 1

Implement the bubble sort, shaker sort, and selection sort as Python functions.
You will also need a function to create a random list of N integers, duplicates allowed.

Put it all together inside a main function.
Also, test to make sure all your sorting functions are working.
Do this by copying the original list, useing the built in Python sort method on the copy,
then checking if your sorted list matches the sorted copy.
Do this multiple times to verify that each of your sorting algorithms are working.
"""

import random
import time


def bubble_sort(nums, reverse=False):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(nums)):
            a, b = nums[i - 1: i + 1]
            if (a > b and not reverse) or (b > a and reverse):
                nums[i] = a
                nums[i - 1] = b
                swapped = True
    return nums


def shaker_sort(nums, reverse=False):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(nums) - 1):
            a = nums[i]
            b = nums[i + 1]
            if (a > b and not reverse) or (b > a and reverse):
                nums[i] = b
                nums[i + 1] = a
                swapped = True

        if not swapped:
            break

        swapped = False
        for i in range(len(nums) - 2, -1, -1):
            a = nums[i]
            b = nums[i + 1]
            if (a > b and not reverse) or (b > a and reverse):
                nums[i] = b
                nums[i + 1] = a
                swapped = True

    return nums


def selection_sort(nums, reverse=False):
    for j in range(0, len(nums)):
        m = j
        for i in range(j + 1, len(nums)):
            a = nums[m]
            b = nums[i]
            if (a > b and not reverse) or (a < b and reverse):
                m = i
        if m != j:
            nums[j], nums[m] = nums[m], nums[j]
    return nums


def create_random(n):
    return [random.randint(1, n) for _ in range(n)]


def main():
    sort_functions = {
        'bubble sort   ': bubble_sort,
        'shaker sort   ': shaker_sort,
        'selection sort': selection_sort,
    }

    reverse = False

    total_sorts = 0
    bad_sorts = 0
    times = {'python sorted ': []}
    for i in range(10):
        list_length = random.randint(10, 2500)
        unsorted_list = create_random(list_length)
        print('List length   ', list_length)
        print('unsorted list ', unsorted_list)

        start = time.time()
        sorted_list = sorted(unsorted_list, reverse=reverse)
        end = time.time()
        times['python sorted '].append(end-start)
        print('python sorted ', sorted_list)

        print()

        for key in sort_functions:
            total_sorts += 1
            start = time.time()
            function_sorted_list = sort_functions[key](unsorted_list[:], reverse=reverse)
            end = time.time()
            run_time = end - start
            if key in times:
                times[key].append(run_time)
            else:
                times[key] = [run_time]
            print(key, function_sorted_list)

            if function_sorted_list != sorted_list:
                bad_sorts += 1

            print(key.strip(), 'OK' if function_sorted_list == sorted_list else 'ERROR')
            print('Took', round(run_time, 2), 'seconds')
            print()

        print()
        print()

    if bad_sorts == 0:
        print('All', total_sorts, 'sorts were successful!')
    else:
        print('There were errors with', bad_sorts, 'of', total_sorts, 'sorts')

    for key in times:
        print(key, round(sum(times[key]), 2), 'seconds total run time')


if __name__ == '__main__':
    main()
