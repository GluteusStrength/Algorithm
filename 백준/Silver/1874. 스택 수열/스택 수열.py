import sys
n = int(sys.stdin.readline())
stack = []
p = []
cnt = 1
flag = True
for _ in range(n):
    d = int(sys.stdin.readline())
    while cnt <= d:
        stack.append("+")
        p.append(cnt)
        cnt += 1
    if p and p.pop() == d:
        stack.append("-")
    else:
        flag = False
if flag:
    for i in stack:
        print(i)
else:
    print("NO")