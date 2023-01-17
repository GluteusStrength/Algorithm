n = int(input())
cnt = 0
c = [int(input()) for _ in range(n)]
if len(c) == 1:
    print(0)
else:
    while c[0] <= max(c[1:]):
        flag = c[1:]
        idx = c[1:].index(max(flag))
        c[0] += 1
        c[idx+1] -= 1
        cnt += 1
    print(cnt)
