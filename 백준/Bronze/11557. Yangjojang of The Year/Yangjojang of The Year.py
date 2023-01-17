N = int(input())
while N > 0:
    t = int(input())
    li = []
    for i in range(t):
        y, z = input().split()
        k = (y, int(z))
        li.append(k)
    if len(li) == t:
        m = []
        ans = 0
        for x in range(t):
            m.append(li[x][1])
        m_most = max(m)
        for x in range(t):
            if m_most == li[x][1]:
                ans = li[x][0]
            else:
                continue
        print(ans)
        N -= 1