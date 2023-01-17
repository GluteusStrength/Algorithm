import sys
N = input()
n = int(N)
l = list(map(int, sys.stdin.readline().split()))
dp_increase = [1] * n
dp_decrease = [1] * n
for i in range(1, n):
    for j in range(i):
        if l[i] > l[j]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)
for x in range(n-1, -1, -1):
    for y in range(n-1, x, -1):
        if l[x] > l[y]:
            dp_decrease[x] = max(dp_decrease[x], dp_decrease[y]+1)
max_ind_1 = dp_increase.index(max(dp_increase))
result = [1] * n
for a in range(n):
    result[a] = dp_increase[a] + dp_decrease[a] - 1
print(max(result))