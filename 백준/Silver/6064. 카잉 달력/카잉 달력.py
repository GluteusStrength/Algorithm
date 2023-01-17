n = int(input())
import sys
import math
cal = []
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    cal.append(l)
for j in range(n):
    w = cal[j]
    m = w[0]
    n = w[1]
    x = w[2]
    y = w[3]
    gcd = math.gcd(m,n)
    lcd = gcd * (m // gcd) * (n // gcd)
    if x <= m and y <= n:
        if m == n:
            if x != y:
                print(-1)
            else:
                print(x)
        else:
            if gcd != 1:
                rpt = []
                if m < n:
                    d = lcd // m
                    rpt.append(x)
                    first_x = x
                    for a in range(d-1):
                        x += m
                        if x > n:
                            x -= n
                            rpt.append(x)
                        else:
                            rpt.append(x)
                    if y in rpt:
                        t = rpt.index(y)
                        ans = t*m + first_x
                        print(ans)
                    else:
                        print(-1)
                else:
                    d = lcd // n
                    rpt.append(y)
                    first_y = y
                    for a in range(d-1):
                        y += n
                        if y > m:
                            y -= m
                            rpt.append(y)
                        else:
                            rpt.append(y)
                    if x in rpt:
                        t = rpt.index(x)
                        ans = t*n + first_y
                        print(ans)
                    else:
                        print(-1)
            else:
                rpt = []
                if m > n:
                    first_y = y
                    rpt.append(y)
                    for a in range(m - 1):
                        y += n
                        if y > m:
                            y -= m
                            rpt.append(y)
                        else:
                            rpt.append(y)
                    ans = n * (rpt.index(x)) + first_y
                    print(ans)
                else:
                    first_x = x
                    rpt.append(x)
                    for a in range(n - 1):
                        x += m
                        if x > n:
                            x -= n
                            rpt.append(x)
                        else:
                            rpt.append(x)
                    ans = m * (rpt.index(y)) + first_x
                    print(ans)
    else:
        print(-1)