import sys; input = sys.stdin.readline
from collections import deque

def topological_sort(graph, degree):
    queue = deque()
    res = []

    for i in range(1, n + 1):
        if degree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        res.append(node)

        for next_node in graph[node]:
            degree[next_node] -= 1
            if degree[next_node] == 0:
                queue.append(next_node)

    return res

n, m = map(int,input().split())
graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

ans = topological_sort(graph, degree)
print(*ans)
