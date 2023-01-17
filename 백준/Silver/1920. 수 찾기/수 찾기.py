import sys
N = int(input())
a = set(list(map(int, sys.stdin.readline().split())))
M = int(input())
b = list(map(int, sys.stdin.readline().split()))
for k in range(M):
    if b[k] in a:
        print(1)
    else:
        print(0)