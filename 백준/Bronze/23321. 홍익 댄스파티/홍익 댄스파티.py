import sys
s = [sys.stdin.readline().rstrip() for _ in range(5)]
length = len(s[0])
status = [list('.omln'), list('owln.'), list('..oLn')]
ans = [[] for _ in range(length)]
for i in range(length):
    for j in range(5):
        ans[i].append(s[j][i])
    if ans[i] == status[0]:
        ans[i] = status[1]
    elif ans[i] == status[1]:
        ans[i] = status[0]
    else:
        continue
for i in range(5):
    st = ""
    for j in range(length):
        st += ans[j][i]
    print(st)