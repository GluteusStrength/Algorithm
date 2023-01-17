import sys
n = int(input())
order = []
stack = []
for i in range(n):
    order.append(list(map(str, sys.stdin.readline().split())))
for i in order:
    if len(i) == 2:
        stack.append(int(i[1]))
    else:
        o = i[0]
        if o == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif o == "size":
            print(len(stack))
        elif o == "empty":
            if stack:
                print(0)
            else:
                print(1)
        else:
            if stack:
                print(stack.pop())
            else:
                print(-1)
