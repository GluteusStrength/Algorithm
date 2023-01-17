import sys
k = int(sys.stdin.readline())
stack = []
for _ in range(k):
    p = int(sys.stdin.readline())
    if p != 0: stack.append(p)
    else: stack.pop()
if stack: print(sum(stack))
else: print(0)