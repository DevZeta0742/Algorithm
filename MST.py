import sys; input = sys.stdin.readline
from collections import defaultdict
import heapq

# Prim MST (우선순위 큐 이용)
def prim(n, tree):
    visited = [0] * (n+1)
    min_heap = [(0, 1)]
    mst_w = 0

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if visited[node]:
            continue

        visited[node] = 1
        mst_w += weight

        for next_node, next_weight in tree[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap, (next_weight, next_node))

    return mst_w

# Kruskal MST (union find 이용)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def Kruskal(n, tree):
    parent = [i for i in range(n + 1)]
    mst_w = 0
    edges = []

    for node in tree:
        for next_node, weight in tree[node]:
            edges.append((weight, node, next_node))

    edges.sort()

    for weight, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            mst_w += weight

    return mst_w

v, e = map(int,input().split()) # 정점, 간선
tree = defaultdict(list)

for _ in range(e):
    a, b, c = map(int,input().split()) # 정점a와 정점b의 가중치c
    tree[a].append((b, c))
    tree[b].append((a, c))

print(prim(v, tree))
