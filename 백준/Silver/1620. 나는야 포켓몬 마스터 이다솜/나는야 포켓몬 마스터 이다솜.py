import sys
input = sys.stdin.readline
from collections import defaultdict
n, m = map(int, input().split())
card = defaultdict()
rev = defaultdict()
for i in range(n):
    x = input().rstrip()
    card[x] = i+1
    rev[i+1] = x
for _ in range(m):
    o = input().rstrip()
    if o.isalpha():
        print(card[o])
    else:
        print(rev[int(o)])