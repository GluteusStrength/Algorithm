s = input()
stack = []
for i in s:
    if i == "-":
        if stack:
            if "".join(stack[-1:]) == "c" or "".join(stack[-1:]) == "d":
                a = stack.pop()
                p = a + i
                stack.append(p)
            else:
                stack.append(i)
        else:
            stack.append(i)
    elif i == "=":
        if len(stack) >= 2:
            if "".join(stack[-2:]) == "dz":
                a = stack.pop()
                b = stack.pop()
                p = b + a + i
                stack.append(p)
            elif "".join(stack[-1:]) == "c" or "".join(stack[-1:]) == "s" or "".join(stack[-1:]) == "z":
                a = stack.pop()
                p = a + i
                stack.append(p)
            else:
                stack.append(i)
        else:
            if stack:
                if "".join(stack[-1:]) == "c" or "".join(stack[-1:]) == "s" or "".join(stack[-1:]) == "z":
                    a = stack.pop()
                    p = a + i
                    stack.append(p)
                else:
                    stack.append(i)
            else:
                stack.append(i)
    elif i == "j":
        if stack:
            if stack[-1] == "l" or stack[-1] == "n":
                x = stack.pop()
                p = x + i
                stack.append(p)
            else:
                stack.append(i)
        else:
            stack.append(i)
    else:
        stack.append(i)
print(len(stack))