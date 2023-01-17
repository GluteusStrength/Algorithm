import sys
n = int(input())
liq = list(map(int, sys.stdin.readline().split()))
start = 0
end = n - 1
min_feat = 200000001
ans_l = start
ans_r = end
while start < end:
    feat = liq[start] + liq[end]
    min_feat = min(abs(feat), min_feat)
    if abs(feat) == min_feat:
        ans_l = start
        ans_r = end
    if feat < 0:
        start += 1
    else:
        end -= 1
print(liq[ans_l] + liq[ans_r])