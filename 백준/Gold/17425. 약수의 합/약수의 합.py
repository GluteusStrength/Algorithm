import sys
n = int(sys.stdin.readline())
nums = [0 for _ in range(1000001)]
for i in range(1, 1000001): # 에라토스테네스의 체처럼?
    for j in range(i, 1000001, i):
        nums[j] += i
    nums[i] += nums[i-1]
for x in range(n):
    k = int(sys.stdin.readline())
    print(nums[k])

