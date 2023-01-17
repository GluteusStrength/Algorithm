import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
c = combinations_with_replacement(nums, m)
c = list(c)
for i in c:
    print(*i)