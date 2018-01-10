a_list = [2, 6, 3, 1, 9, 4, 8]


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

print(linear_search(a_list, 4))
