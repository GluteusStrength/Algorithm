import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
s = sum(nums)
res = 0
for i in nums:
    s -= i
    res += s*i
print(res)