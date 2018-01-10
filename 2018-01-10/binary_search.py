b_list = [1, 2, 3, 4, 5, 6, 9]


def binary_search(b, x):
    low = 0
    high = len(b) - 1
    while low <= high:
        mid = (low + high) // 2
        if b[mid] == x:
            return mid
        elif b[mid] > x:
            high = mid - 1
        elif b[mid] < x:
            low = mid + 1
    return -1


print(binary_search(b_list, 4))
