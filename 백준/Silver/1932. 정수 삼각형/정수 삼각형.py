import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(list(map(int, sys.stdin.readline().split())))
for i in range(1,n):
    for j in range(len(nums[i])):
        if j == 0:
            nums[i][j] += nums[i-1][j]
        elif i == j:
            nums[i][j] += nums[i-1][j-1]
        else:
            case_1 = nums[i][j] + nums[i-1][j-1]
            case_2 = nums[i][j] + nums[i-1][j]
            nums[i][j] = max(case_1, case_2)
print(max(nums[-1]))