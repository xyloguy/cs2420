"""
Sorting 2

Implement these additional sorting algorithms: Quick, Modified Quick, Merge, and Hash.
Test your sorting algorithms as you did in the previous assignment.
"""

import random
import time


def quick_sort(nums, reverse=False):
    less = []
    equal = []
    greater = []

    if len(nums) > 1:
        pivot = nums[0]
        for x in nums:
            if x < pivot and not reverse or x > pivot and reverse:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        return quick_sort(less, reverse) + equal + quick_sort(greater, reverse)
    else:
        return nums


def modified_quick_sort(nums, reverse=False):
    # I wasn't sure what "modified" meant, I thought maybe it wanted us to use
    # a median pivot point instead of the first item in the array to be sorted,
    # that is the only difference between my previous quick_sort and this one.
    size = len(nums)
    if size <= 1:
        return nums

    # if size >= 3:
    #     first = nums[0]
    #     middle = nums[size // 2]
    #     last = nums[size-1]
    #     if first < middle:
    #         if middle < last:
    #             pivot = middle
    #         elif first < last:
    #             pivot = last
    #         else:
    #             pivot = first
    #     else:
    #         if first < last:
    #             pivot = first
    #         elif middle < last:
    #             pivot = last
    #         else:
    #             pivot = middle
    # else:
    #     pivot = nums[0]

    middle = size//2
    first = nums[0]
    nums[0] = nums[middle]
    nums[middle] = first
    pivot = nums[0]

    less = []
    equal = []
    greater = []


    for num in nums:
        if num < pivot and not reverse or num > pivot and reverse:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    return quick_sort(less, reverse) + equal + quick_sort(greater, reverse)



def merge_sort(nums, reverse=False):
    if len(nums) > 1:
        middle = len(nums)//2

        a = nums[:middle]
        b = nums[middle:]
        a = merge_sort(a, reverse)
        b = merge_sort(b, reverse)

        i = 0
        j = 0
        k = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j] and not reverse or b[j] < a[i] and reverse:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = b[j]
                j += 1
            k += 1
        while i < len(a):
            nums[k] = a[i]
            i += 1
            k += 1
        while j < len(b):
            nums[k] = b[j]
            j += 1
            k += 1
    return nums


def hash_sort(nums, reverse=False):
    if len(nums) <= 1:
        return nums

    smallest = nums[0]
    largest = smallest
    my_hash = {}
    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

        if num in my_hash:
            my_hash[num] += 1
        else:
            my_hash[num] = 1

    output = []
    if reverse:
        generator = range(largest, smallest - 1, -1)
    else:
        generator = range(smallest, largest + 1)
    for i in generator:
        if i not in my_hash:
            continue
        output += [i] * my_hash[i]
    return output


def create_random(n):
    return [random.randint(1, n) for _ in range(n)]


def main():
    sort_functions = {
        'quick sort         ': quick_sort,
        'modified quick sort': modified_quick_sort,
        'merge sort         ': merge_sort,
        'hash sort          ': hash_sort,
    }

    reverse = False

    total_sorts = 0
    bad_sorts = 0
    times = {'python sorted      ': []}
    for i in range(10):
        list_length = random.randint(10, 500000)
        unsorted_list = create_random(list_length)
        print('List length:', list_length)

        start = time.time()
        sorted_list = sorted(unsorted_list[:], reverse=reverse)
        end = time.time()
        total = end-start
        times['python sorted      '].append(total)
        print('python sorted,', round(total, 2), 'seconds')

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
            if function_sorted_list != sorted_list:
                bad_sorts += 1

            print(
                key.strip(),
                'OK,' if function_sorted_list == sorted_list else 'ERROR,',
                round(run_time, 2), 'seconds'
            )

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
