import sys
n = int(input())
d = {}
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if d == {}:
        d[b] = a
    else:
        d_l = list(d.keys())
        if b not in d_l:
            d[b] = a
        else:
            plus = d[b] + a
            d[b] = plus
final = list(d.items())
ans = 0
for j in range(len(final)):
    c = final[j][1]
    k = final[j][0]
    if k > 1:
        c *= k
        k -= 1
        ans += ((c * (1 ** k)))
    else:
        if k == 1:
            ans += c
        if k == 0:
            ans += 0
print(ans)
