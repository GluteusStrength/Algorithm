import sys
n, m = map(int, sys.stdin.readline().split())
r = list(map(int, sys.stdin.readline().split()))
party = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
if len(r) == 0:
    print(m)
else:
    r = r[1:]
    root = [i for i in range(n+1)]
    def find(x):
        if root[x] != x:
            root[x] = find(root[x])
        return root[x]
    def union(x, y):
        x = find(x)
        y = find(y)
        if x in r and y in r:
            return
        else:
            if x in r:
                root[y] = x
            elif y in r:
                root[x] = y
            else:
                root[y] = x
    for i in party:
        ch = i[1:]
        if len(ch) == 1:
            continue
        else:
            for j in range(1, len(ch)):
                for k in range(j):
                    union(ch[j], ch[k])
    cnt = 0
    for i in party:
        flag = True
        for j in i[1:]:
            k = find(j)
            if k in r:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)