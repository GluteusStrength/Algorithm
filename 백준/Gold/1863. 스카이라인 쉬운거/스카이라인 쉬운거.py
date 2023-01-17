import sys
n = int(sys.stdin.readline())
skyline = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
skyline.sort(key = lambda x : x[0])
stack = []
res = 0
for i in range(n):
    x, y = skyline[i][0], skyline[i][1]
    while stack and stack[-1] > y:
        res += 1
        stack.pop()
    if stack and stack[-1] == y:
        continue
    stack.append(y)
while stack:
    x = stack.pop()
    if x > 0:
        res += 1
print(res)
