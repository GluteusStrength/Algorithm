import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
stack = [0]
ans = [-1 for _ in range(n)]
for i in range(1, n):
    while stack and l[stack[-1]] < l[i]:
        ans[stack.pop()] = l[i]
    stack.append(i)
print(*ans)


