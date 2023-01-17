import sys
n = int(sys.stdin.readline())
d = [0] * 10001
for _ in range(n):
    x = int(sys.stdin.readline())
    d[x] += 1
for i in range(1, 10001):
    if d[i] != 0:
        for j in range(d[i]):
            print(i)