from collections import deque

# def bfs(graph, start, path=[]):
#     q = [start]
#     while q:
#         v = q.pop(0)  # use queue
#         if v not in path:
#             path.append(v)
#             q += graph[v]
#     return path


def bfs(g, start):
    queue, enqueued = deque([(None, start)]), {start}
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])


def shortest_path_bfs(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None


if __name__ == '__main__':
    # a sample graph
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F', 'D'],
             'F': ['C']}

    print('bfs', shortest_path_bfs(graph, 'A', 'D'))
