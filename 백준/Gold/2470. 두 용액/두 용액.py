import sys
n = int(sys.stdin.readline())
liq = list(map(int, sys.stdin.readline().split()))
liq.sort()
left = 0
right = n-1
ans_left = left
ans_right = right
min_liq = 2000000001 # 모든 것이 1000000000으로 초기화 돼있다고 가정했을 때!
while left < right:
    if liq[left] + liq[right] == 0:
        print(liq[left], liq[right])
        break
    else:
        if liq[left] + liq[right] < 0:
            s = abs(liq[left] + liq[right])
            min_liq = min(s, min_liq)
            if s == min(s, min_liq):
                ans_left = left
                ans_right = right
            left += 1
        else:
            s = abs(liq[left] + liq[right])
            min_liq = min(s,min_liq)
            if s == min(s, min_liq):
                ans_left = left
                ans_right = right
            right -= 1
print(liq[ans_left], liq[ans_right])



