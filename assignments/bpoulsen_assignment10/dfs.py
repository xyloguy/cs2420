# def dfs(graph, start, path=[]):
#     q = [start]
#     while q:
#         v = q.pop()  # use stack
#         if v not in path:
#             path.append(v)
#             q += graph[v]
#     return path


def dfs(g, start):
    stack, enqueued = [(None, start)], {start}
    while stack:
        parent, n = stack.pop()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        stack.extend([(n, child) for child in new])


def shortest_path_dfs(g, start, end):
    parents = {}
    for parent, child in dfs(g, start):
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

    print('dfs', shortest_path_dfs(graph, 'A', 'D'))
