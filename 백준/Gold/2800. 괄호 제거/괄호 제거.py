# 굳이 조합으로 가야하는가?
from itertools import combinations
e = input()
stack_front = []
stack = []
ans = []
e_list = list(e)
for i in range(len(e)):
    if e[i] == "(":
        stack_front.append(i)
    if e[i] == ")":
        x = stack_front.pop()
        t = (x, i)
        stack.append(t)
for i in range(1, len(stack)+1):
    comb = list(combinations(stack, i))
    if i == 1:
        for j in comb:
            x = j[0]
            e_list[x[0]] = ""
            e_list[x[1]] = ""
            ans.append("".join(e_list))
            e_list = list(e)
    else:
        for j in comb:
            for k in j:
                e_list[k[0]] = ""
                e_list[k[1]] = ""
                ans.append("".join(e_list))
            e_list = list(e)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)