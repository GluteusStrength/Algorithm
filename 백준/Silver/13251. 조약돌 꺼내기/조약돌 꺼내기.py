import sys
m = int(input())
n = list(map(int, sys.stdin.readline().split()))
k = int(input())
sum_all = sum(n)
down = sum_all
for i in range(k-1):
    sum_all -= 1
    down *= sum_all
up = 0
for x in range(m):
    upper = n[x]
    upper_c = n[x]
    for y in range(k-1):
        upper_c -= 1
        upper *= upper_c
    up += upper
print(up/down)