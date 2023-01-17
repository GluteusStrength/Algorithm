import sys
n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
w.sort()
for i in range(1, n):
    w[i] += w[i-1]
print(sum(w))