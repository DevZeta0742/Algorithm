import bisect

def lis(arr):  # nlogn
    lst = []
    for num in arr:
        pos = bisect.bisect_left(lst, num)
        if pos == len(lst):
            lst.append(num)

        else:
            lst[pos] = num

    return lst

###################################################

dp = [1] * n  # O(n^2)
box = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        
print(max(dp))
#                                                    lis length
# ---------------------------------------------------
#                                                    lis sequence
import sys; input = sys.stdin.readline
from bisect import bisect_left

def LIS(seq): # nlogn
    n = len(seq)
    lst = []
    pos = [0] * n
    prev = [-1] * n

    for i in range(n):
        idx = bisect_left(lst, seq[i])
        if idx == len(lst):
            lst.append(seq[i])

        else:
            lst[idx] = seq[i]

        pos[idx] = i
        if idx > 0:
            prev[i] = pos[idx - 1]

    res = []
    idx = pos[len(lst) - 1]
    while idx != -1:
        res.append(seq[idx])
        idx = prev[idx]

    res.reverse()

    return res

n = int(input())
sequence = list(map(int,input().split()))

ans = LIS(sequence)

print(len(ans))
print(*ans)
