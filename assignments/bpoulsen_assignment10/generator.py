from random import randint as r, choice
from string import ascii_uppercase as uppercase

pos_verticies = uppercase
n = r(5, len(pos_verticies))
verticies = pos_verticies[:n]
print(n)

edges = []
pos_tests = []
for v in verticies:
    for v2 in verticies:
        s = '{} {}'.format(v, v2)

        if v == v2:
            continue
        if r(0, 5) == 1 and s not in edges:
            edges.append(s)
        pos_tests.append(s)

print(len(edges))
for edge in edges:
    print(edge)

n_tests = r(5, len(edges))
print(n_tests)
tests = []
for i in range(n_tests):
    r = choice(pos_tests)
    while r in tests:
        r = choice(pos_tests)
    tests.append(r)

for test in tests:
    print(test)
