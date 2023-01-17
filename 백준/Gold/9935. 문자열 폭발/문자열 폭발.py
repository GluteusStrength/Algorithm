import sys
s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
stack = []
for i in range(len(s)):
    stack.append(s[i])
    if stack[-1] == p[-1] and "".join(stack[-len(p):]) == p:
        for j in range(len(p)):
            stack.pop()
ans = "".join(stack)
if ans == "":
    print("FRULA")
else:
    print(ans)
