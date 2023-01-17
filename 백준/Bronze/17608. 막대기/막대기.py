import sys
n = int(sys.stdin.readline())
stack = []
stick = [int(sys.stdin.readline()) for _ in range(n)]
for i in stick:
    if not stack:
        stack.append(i)
    else:
        while stack and stack[-1] <= i:
            stack.pop()
        stack.append(i)
print(len(stack))