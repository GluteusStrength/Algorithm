import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
l = list(map(int, input().split()))
l_real = list(set(l))
d = defaultdict()
l_real.sort()
d[l_real[0]] = 0
for i in range(1, len(l_real)):
    d[l_real[i]] = i
for i in l:
    print(d[i], end = " ")