import sys, math
n = int(sys.stdin.readline())
prob = list(map(int, sys.stdin.readline().split()))
nums = [i for i in range(1, n+1)]
l = []
cnt = 0
if prob[0] == 1:
    while len(l) != n:
        for i in nums:
            x = math.factorial(len(nums) - 1)
            if cnt + x < prob[1]:
                cnt += x
            else:
                nums.remove(i)
                l.append(i)
                break
    print(*l)
else:
    flag = prob[1:]
    cnt = 0
    while nums:
        for i in nums:
            if i == flag[0]:
                nums.remove(i)
                flag.pop(0)
                break
            else:
                cnt += math.factorial(len(nums) - 1)
    print(cnt+1)