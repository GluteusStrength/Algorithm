import sys
N = input()
n = int(N)
l = list(map(int, sys.stdin.readline().split()))
dp_decrease = [1] * n
for x in range(n-1, -1, -1):
    for y in range(n-1, x, -1):
        if l[x] > l[y]:
            dp_decrease[x] = max(dp_decrease[x], dp_decrease[y]+1)
print(max(dp_decrease))