n = int(input())
e = input()
nums = [int(input()) for _ in range(n)]
stack = []
res = 0
for i in e:
    if i.isalpha():
        stack.append(nums[ord(i)-65])
    else:
        x = stack.pop()
        y = stack.pop()
        if i == "+":
            stack.append(y+x)
        elif i == "-":
            stack.append(y-x)
        elif i == "*":
            stack.append(y*x)
        else:
            stack.append(y/x)
print(format(stack[0], ".2f"))
