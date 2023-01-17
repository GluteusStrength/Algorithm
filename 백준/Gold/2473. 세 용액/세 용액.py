import sys
n = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()
s = 0
e = n - 1
ans_l = 0
ans_r = n - 1
ans_m = (ans_l + ans_r) // 2
min_liq = 3000000001
zero = 0
for i in range(n-2):
    s = i + 1
    e = n - 1
    while s < e:
        feat = liq[i] + liq[s] + liq[e]
        min_liq = min(min_liq, abs(feat))
        if abs(feat) == min_liq:
            ans_l = i
            ans_m = s
            ans_r = e
        if feat < 0:
            s += 1
        elif feat > 0:
            e -= 1
        else:
            zero += 1
            break
    if zero > 1:
        break
print(liq[ans_l], liq[ans_m], liq[ans_r])