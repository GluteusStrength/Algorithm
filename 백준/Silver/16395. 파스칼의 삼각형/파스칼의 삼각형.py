import sys
import math
n, k = map(int, sys.stdin.readline().split())
if n == 0 or n == 1:
    print(1)
else:
    n -= 1
    k -= 1
    x = math.factorial(n)
    y = math.factorial(n-k)
    z = math.factorial(k)
    print(int(x/(y*z)))
