import sys
l = list(map(int, sys.stdin.readline().split()))
n = l[0]
m = l[1]
if n == m:
    print(1)
else:
    import math
    up = math.factorial(n)
    down = math.factorial(m)*math.factorial(n-m)
    ans = int(up//down)
    print(ans)