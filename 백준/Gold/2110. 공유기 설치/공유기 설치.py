import sys
n, c = map(int, sys.stdin.readline().split())
home = []
for _ in range(n):
    home.append(int(sys.stdin.readline()))
home.sort()
s = 1
e = home[-1] - home[0]
tmp = 1000000001
res = 0
if c == 2:
    print(e)
else:
    while s <= e:
        mid = (s + e) // 2
        flag = home[0]
        cnt = 1
        for i in range(1, n):
            if flag + mid <= home[i]:
                cnt += 1
                flag = home[i]
        if cnt >= c:
            res = mid
            s = mid + 1
        else:
            e = mid - 1
    print(res)

