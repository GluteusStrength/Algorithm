import sys, math
from itertools import combinations
n = int(input())
d = []
for i in range(n):
    t = int(input())
    for j in range(t):
        a,b = map(int, sys.stdin.readline().split())
        d.append((a,b))
    if t == 2:
        dist_x = (d[0][0] - d[1][0])
        dist_y = (d[0][1] - d[1][1])
        dist = math.sqrt(dist_x*dist_x+dist_y*dist_y)
        print(dist)
        d = []
    else:
        comb = list(combinations(d, t//2))
        s = len(comb) // 2
        rev_s = len(comb) - 1
        ans = math.inf
        for x in comb[:s]:
            x_sum = 0
            y_sum = 0
            for y in range(len(x)):
                x_sum += x[y][0]
                y_sum += x[y][1]
            rev = comb[rev_s]
            x_del = 0
            y_del = 0
            for z in range(len(rev)):
                x_del += rev[z][0]
                y_del += rev[z][1]
            rev_s -= 1
            mag = math.sqrt((x_sum-x_del)*(x_sum-x_del) + (y_sum-y_del)*(y_sum-y_del))
            ans = min(ans, mag)
        print(ans)
        d = []


