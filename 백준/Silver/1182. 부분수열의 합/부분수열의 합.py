import sys
from itertools import combinations
n, s = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]
n_l = [0] + list(map(int, sys.stdin.readline().split()))
res = 0
for i in n_l[1:]:
    if i == s:
        res += 1
for i in range(2, n+1):
    x = list(combinations(nums, i))
    for j in x:
        flag = 0
        for k in j:
            flag += n_l[k]
        if flag == s:
            res += 1
print(res)

