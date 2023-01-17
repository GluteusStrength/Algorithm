import sys
n, m = map(int, sys.stdin.readline().split())
site = [[],[]]
for i in range(n):
    x, y = map(str, sys.stdin.readline().split())
    site[0].append(x)
    site[1].append(y)
f = [sys.stdin.readline().rstrip() for _ in range(m)]
for i in f:
    a = site[0].index(i)
    print(site[1][a])

