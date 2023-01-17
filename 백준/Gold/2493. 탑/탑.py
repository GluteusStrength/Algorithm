import sys
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
tower = list(reversed(tower))
stack = []
ans = [0 for _ in range(n)]
for i in range(n):
    while stack and tower[stack[-1]] < tower[i]:
        ans[stack.pop()] = n - i
    stack.append(i)
ans = list(reversed(ans))
print(*ans)
