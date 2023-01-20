import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]
t = 0
for _ in range(m):
    c = input().strip()
    if c in s:
        t += 1
print(t)