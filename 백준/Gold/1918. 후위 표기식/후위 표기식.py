e = input()
res = ""
stack = []
op_top = ["*", "/"]
op_bottom = ["+", "-"]
for i in e:
    if i.isalpha():
        res += i
    else:
        if i == "(":
            stack.append(i)
        elif i in op_top:
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(i)
        elif i in op_bottom:
            while stack and stack[-1] != "(": # 왼쪽 괄호는 우선순위에서 제일 아래
                res += stack.pop()
            stack.append(i)
        else:
            while stack and stack[-1] != "(": # 괄호 안의 연산자의 우선순위는 위에서 처리.
                res += stack.pop()
            stack.pop() # (를 빼준다
while stack: # 남아있는 것들 처리
    res += stack.pop()
print(res)