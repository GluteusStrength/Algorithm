import sys
n, m, k = map(int, sys.stdin.readline().split())
if n < m + k - 1 or n > m * k:
    print(-1)
else:
    l = list(range(1, n+1))
    group = [[] for _ in range(m)]
    if n % m == 0 and n % k == 0:
        for i in range(m):
            for j in range(k):
                group[i].append(l[0])
                l.remove(l[0])
            group[i].sort(reverse = True)
        ans_list = sum(group, [])
        print(*ans_list)
    else:
        for i in range(k):
            group[0].append(l[0])
            l.remove(l[0])
        group[0].sort(reverse=True)
        a = n - k
        b = m - 1
        for i in range(1, m):
            if b == 0:
                break
            else:
                div = a // b
                for j in range(div):
                    group[i].append(l[0])
                    l.remove(l[0])
                group[i].sort(reverse = True)
                a -= div
                b -= 1
        ans = sum(group, [])
        print(*ans)