t = int(input())
for _ in range(t):
    flag = True
    stack = []
    s = input()
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                flag = False
            else:
                stack.pop()
    if stack:
        flag = False
    if flag == False:
        print("NO")
    else:
        print("YES")
