import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))
comb = combinations(card, 3)
ans = 0
for i in comb:
    flag = sum(i)
    if flag == m:
        ans = flag
        break
    else:
        if flag > m:
            continue
        else:
            if (m - ans) > (m - flag):
                ans = flag
print(ans)
