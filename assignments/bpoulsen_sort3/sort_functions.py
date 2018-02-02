def bubble_sort(nums, count):
    swapped = True
    while swapped:
        count.compares = 1
        swapped = False
        for i in range(1, len(nums)):
            count.compares = 1
            if nums[i - 1] > nums[i]:
                count.swaps = 1
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapped = True
    return nums


def shaker_sort(nums, count):
    swapped = True
    while swapped:
        count.compares = 1
        swapped = False
        for i in range(0, len(nums) - 1):
            count.compares = 1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count.swaps = 1
                swapped = True

        count.compares = 1
        if not swapped:
            break

        swapped = False
        for i in range(len(nums) - 2, -1, -1):
            count.compares = 1
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                count.swaps = 1
                swapped = True
    return nums


def selection_sort(nums, count):
    for j in range(0, len(nums)):
        m = j
        for i in range(j + 1, len(nums)):
            count.compares = 1
            if nums[m] > nums[i]:
                m = i
        if m != j:
            nums[j], nums[m] = nums[m], nums[j]
            count.swaps = 1
    return nums


def quick_sort(nums, count):
    less = []
    equal = []
    greater = []

    count.compares = 1
    if len(nums) > 1:
        pivot = nums[0]
        for x in nums:
            count.compares = 1
            count.swaps = 1
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        nums = quick_sort(less, count) + equal + quick_sort(greater, count)
        return nums
    else:
        return nums


def modified_quick_sort(nums, count):
    size = len(nums)

    count.compares = 1
    if size <= 1:
        return nums

    middle = size//2
    nums[0], nums[middle] = nums[middle], nums[0]
    count.swaps = 1
    pivot = nums[0]

    less = []
    equal = []
    greater = []

    for num in nums:
        count.compares = 1
        count.swaps = 1
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)
    return modified_quick_sort(less, count) + equal + modified_quick_sort(greater, count)


def merge_sort(nums, count):
    count.compares = 1
    if len(nums) > 1:
        middle = len(nums)//2

        a = nums[:middle]
        b = nums[middle:]
        count.swaps = len(nums)
        a = merge_sort(a, count)
        b = merge_sort(b, count)

        i = 0
        j = 0
        k = 0

        while i < len(a) and j < len(b):
            count.compares = 2
            count.swaps = 1
            if a[i] < b[j]:
                nums[k] = a[i]
                i += 1
            else:
                nums[k] = b[j]
                j += 1
            k += 1

        while i < len(a):
            count.compares = 1
            count.swaps = 1
            nums[k] = a[i]
            i += 1
            k += 1

        while j < len(b):
            count.compares = 1
            count.swaps = 1
            nums[k] = b[j]
            j += 1
            k += 1
    return nums


def hash_sort(nums, count):
    count.compares = 1
    if len(nums) <= 1:
        return nums

    smallest = nums[0]
    largest = smallest
    my_hash = {}
    for num in nums:
        count.compares = 1
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

        count.swaps = 1
        if num in my_hash:
            my_hash[num] += 1
        else:
            my_hash[num] = 1

    output = []
    generator = range(smallest, largest + 1)
    for i in generator:
        count.compares = 1
        if i not in my_hash:
            continue

        count.swaps = my_hash[i]
        output += [i] * my_hash[i]
    return output
