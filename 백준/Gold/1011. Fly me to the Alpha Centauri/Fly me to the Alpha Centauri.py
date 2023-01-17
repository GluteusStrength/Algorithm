import sys
import math
t = int(input())
for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    dist = y - x
    a = math.sqrt(dist)
    if dist <= 3:
        print(dist)
    else:
        if a == int(a):
            print(int(2*a - 1))
        if a > int(a):
            st = int(a)*(int(a+1))
            if dist <= st:
                ans = (int(a)*2)
                print(ans)
            else:
                ans = int(a)*2 + 1
                print(ans)
