import sys; input = sys.stdin.readline
from collections import defaultdict
import heapq

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

def Kruskal(): # 나중에..
  

v, e = map(int,input().split()) # 정점, 간선
tree = defaultdict(list)

for _ in range(e):
    a, b, c = map(int,input().split()) # 정점a와 정점b의 가중치c
    tree[a].append((b, c))
    tree[b].append((a, c))

print(prim(v, tree))
