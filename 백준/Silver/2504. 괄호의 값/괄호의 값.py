t = input()
cnt = 1
ans = 0
standard = True
l_1 = []
l_2 = []
for i in range(len(t)):
    if t[i] == "(":
        l_1.append(t[i])
        cnt *= 2
    elif t[i] == "[":
        l_2.append(t[i])
        cnt *= 3
    elif t[i] == ")":
        if l_1:
            if t[i-1] == "(":
                ans += cnt
            l_1.pop()
            cnt //= 2
        else:
            standard = False
            break
    elif t[i] == "]":
        if l_2:
            if t[i-1] == "[":
                ans += cnt
            l_2.pop()
            cnt //= 3
        else:
            standard = False
            break
if not l_1 and not l_2 and standard:
    print(ans)
else:
    print(0)

