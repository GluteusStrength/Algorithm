import sys
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
x, y = map(int, sys.stdin.readline().split())
sang = int(n * x / 100)
jeol = 0
for i in s:
    if i >= y:
        jeol += 1
final = [sang, jeol]
print(*final)
