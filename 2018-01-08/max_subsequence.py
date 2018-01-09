import random
import time


def max_sub_sequence_n_cubed(l):
    best = (l[0], 0, 0)
    for s in range(len(l)):
        for e in range(s, len(l)):
            sum_of = 0
            for i in range(s, e + 1):
                sum_of += l[i]
            if sum_of > best[0]:
                best = (sum_of, s, e)
    return best


def max_sub_sequence_n_squared(l):
    best = (l[0], 0, 0)
    for s in range(len(l)):
        c = 0
        for e in range(s, len(l)):
            c += l[e]
            if c > best[0]:
                best = (c, s, e)
    return best


def max_sub_sequence_n(l):
    best = (l[0], 0, 0)
    start = 0
    total = best[0]
    for end in range(1, len(l)):
        total += l[end]
        if total > best[0]:
            best = (total, start, end)
        if total <= 0:
            start = end + 1
            total = 0
    return best


if __name__ == '__main__':
    tests = [
        [5, -1, -2, 4, 3, -2, -9, 2, 1, -1, 3, -2, 6, 2, -3, 4, -6, -7, 4, 3, -2, 4],
        [(random.randint(1, 100) * random.choice([-1, 1])) for i in range(1000)],
        [5],
        [-1],
    ]

    algorithms = [
        max_sub_sequence_n_cubed,
        max_sub_sequence_n_squared,
        max_sub_sequence_n,
    ]

    for a in algorithms:
        start_time = time.time()
        for test in tests:
            print(a(test))
        end_time = time.time()
        print(end_time - start_time)
        print()
        print()
