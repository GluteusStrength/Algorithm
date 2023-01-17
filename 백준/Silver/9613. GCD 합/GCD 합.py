import sys, math
from itertools import combinations
n = int(input())
l = []
for i in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    l.append(num)
for j in l:
    gcd_list = []
    x = j[0]
    y = j[1:]
    comb = list(combinations(y,2))
    for k in comb:
        a = k[0]
        b = k[1]
        gcd_list.append(math.gcd(a,b))
    print(sum(gcd_list))