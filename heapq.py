import heapq

# 최소 힙
pq1 = []

heapq.heappush(pq1, 5)
heapq.heappush(pq1, 1)
heapq.heappush(pq1, 10)

print(heapq.heappop(pq1))  # 1
print(heapq.heappop(pq1))  # 5
print(heapq.heappop(pq1))  # 10


# 최대 힙
pq2 = []

heapq.heappush(pq2, -5)
heapq.heappush(pq2, -1)
heapq.heappush(pq2, -10)

print(-heapq.heappop(pq2))  # 10
print(-heapq.heappop(pq2))  # 5
print(-heapq.heappop(pq2))  # 1


# tuple priority queue
tuple_pq = []

# (우선순위, 데이터)
heapq.heappush(tuple_pq, (2, "A"))
heapq.heappush(tuple_pq, (1, "B"))
heapq.heappush(tuple_pq, (3, "C"))

print(heapq.heappop(tuple_pq))  # (1, 'B')
print(heapq.heappop(tuple_pq))  # (2, 'A')
print(heapq.heappop(tuple_pq))  # (3, 'C')
