import sys
n = int(sys.stdin.readline())
nums = [0]+list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
prefix = [0 for _ in range(n+1)]
for i in range(1, n+1):
    prefix[i] = nums[i] + prefix[i-1]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix[j] - prefix[i-1])