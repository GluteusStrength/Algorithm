import sys
l = list(map(int, sys.stdin.readline().split()))
a = l[0]
b = l[1]
c = l[2]
if b >= c:
    print(-1)
else:
    x = c - b
    ans = int(a / x) + 1
    print(ans)