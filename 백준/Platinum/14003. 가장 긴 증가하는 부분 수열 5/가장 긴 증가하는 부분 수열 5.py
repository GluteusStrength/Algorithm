import sys
from bisect import bisect_left
n = int(sys.stdin.readline())
l = [0]+list(map(int, sys.stdin.readline().split()))
dp = [-1000000001]
rec = [0 for _ in range(n+1)] # index 저장용
length = 0
for i in range(1, n+1):
    if dp[-1] < l[i]:
        dp.append(l[i])
        rec[i] = len(dp) - 1 # 어차피 큰 수는 그냥 append 되기 때문에 길이는 이렇게 저장해도 무방
        length = rec[i]
    else:
        rec[i] = bisect_left(dp, l[i]) # 정렬된 dp에 l[i]가 들어갈 위치를 반환한다.
        dp[rec[i]] = l[i]
print(length)
ans = []
for i in range(n, 0, -1): # 14002번에서의 출력 방식
    if rec[i] == length:
        ans.append(l[i])
        length -= 1
    if length == -1:
        break
print(*ans[::-1])

