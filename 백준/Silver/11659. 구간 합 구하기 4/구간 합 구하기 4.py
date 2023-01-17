import sys
n, m = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))
sum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    sum[i] = nums[i] + sum[i-1]
for j in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sum[b] - sum[a-1])