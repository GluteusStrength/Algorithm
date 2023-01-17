import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
w = 0
for num in nums:
    if w + 1 >= num:
        w += num
    else:
        break
print(w+1)