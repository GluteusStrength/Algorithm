import sys
n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().rstrip()
stack = []
cnt = 0
for i in range(n):
    while cnt < k and stack and int(stack[-1]) < int(num[i]):
        cnt += 1
        stack.pop()
    stack.append(num[i])
ans = int("".join(stack))
if len(stack) == (n-k):
    print(ans)
else:
    ans = stack[:n-k]
    print(int("".join(ans)))