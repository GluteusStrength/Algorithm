import sys
n = int(input())
c = []
for i in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))
for i in range(1,n):
    cost = c[i]
    r = cost[0]
    g = cost[1]
    b = cost[2]
    c[i][0] = r + min(c[i-1][1], c[i-1][2])
    c[i][1] = g + min(c[i-1][2], c[i-1][0])
    c[i][2] = b + min(c[i-1][1], c[i-1][0])
print(min(c[-1]))