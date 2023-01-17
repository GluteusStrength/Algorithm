from datetime import datetime
import sys, math
n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    a = []
    for i in range(n):
        x, y, z = map(str, sys.stdin.readline().split())
        a.append([x,y,int(z)])
    cur = a[-1]
    curr = datetime.strptime(cur[0], "%Y/%m/%d")
    table = []
    for i in range(n):
        past = datetime.strptime(a[i][0], "%Y/%m/%d")
        diff = (curr - past).days
        t_1 = datetime.strptime(cur[1], "%H:%M:%S")
        t_2 = datetime.strptime(a[i][1], "%H:%M:%S")
        dif = t_1 - t_2
        if dif.days == -1:
            diff -= 1
        s = dif.seconds
        s /= 3600*24
        diff += s
        diff /= 365
        table.append(max(math.pow(0.5, diff), math.pow(0.9, n-1 - i)))
    down = sum(table)
    up = 0
    for x in range(n):
        u = table[x] * a[x][2]
        up += u
    print(int(round(up/down, 0)))