from bfs import shortest_path_bfs as bfs
from dfs import shortest_path_dfs as dfs

graph = {}
N = int(input())
for _ in range(int(input())):
    a, b = input().split()
    if a not in graph:
        graph[a] = [b]
        continue
    if b in graph[a]:
        continue
    graph[a].append(b)

print('graph', graph)

for _ in range(int(input())):
    start, end = input().split()
    print('bfs', start, end, bfs(graph, start, end))
    print('dfs', start, end, dfs(graph, start, end))
