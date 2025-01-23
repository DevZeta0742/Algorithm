import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
parents = [i for i in range(100001)]

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
