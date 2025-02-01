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
