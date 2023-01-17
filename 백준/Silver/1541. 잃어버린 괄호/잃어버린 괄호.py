import sys
sik = sys.stdin.readline().rstrip()
x = sik.split('-') # -를 기준으로 분리
ans = 0
for i in range(len(x)):
    if "+" in x[i]:
        y = x[i].split("+")
        for j in range(len(y)):
            y[j] = int(y[j])
        res = sum(y)
        if i == 0:
            ans += res
        else:
            ans -= res
    else:
        if i == 0:
            ans += int(x[i])
        else:
            ans -= int(x[i])
print(ans)