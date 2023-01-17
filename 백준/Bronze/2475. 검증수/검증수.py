import sys
nums = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in nums:
    ans += i*i
print(ans % 10)