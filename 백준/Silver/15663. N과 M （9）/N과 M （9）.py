import sys
from itertools import permutations
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
c = permutations(nums, m)
c = list(set(c))
c.sort(key = lambda x : x[0])
for i in c:
    print(*i)

