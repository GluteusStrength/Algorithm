import sys
from collections import Counter
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
ans = [-1 for _ in range(n)]
stack = [0]
d = Counter(A)
for i in range(1, n):
    while stack and d[A[stack[-1]]] < d[A[i]]:
        ans[stack.pop()] = A[i]
    stack.append(i)
print(*ans)