from itertools import combinations
n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]
c = combinations(nums, m)
for i in list(c):
    print(*i)