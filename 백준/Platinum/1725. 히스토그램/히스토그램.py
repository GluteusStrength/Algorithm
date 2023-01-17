import sys
n = int(sys.stdin.readline())
stack = [0]
area = 0
h = []
for i in range(n):
    h.append(int(sys.stdin.readline()))
for i in range(n):
    while stack and h[i] < h[stack[-1]]:
        height = h[stack[-1]]
        stack.pop()
        width = i
        if stack:
            width = i - stack[-1] - 1
        area = max(area, width*height)
    stack.append(i)
while stack:
    height = h[stack[-1]]
    stack.pop()
    width = n
    if stack:
        width = n - (stack[-1] + 1)
    area = max(area, width*height)
p = min(h) * n
area = max(p, area)
print(area)


