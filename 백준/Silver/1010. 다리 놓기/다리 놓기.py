import math
import sys
t = int(input())
for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    up = math.factorial(m)
    down = math.factorial(n)*math.factorial(m-n)
    print(up//down)