import sys
n = int(input())
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    a, b = int(x[0]), int(x[-1])
    print(a+b)