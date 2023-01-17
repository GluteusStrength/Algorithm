import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    m = max(nums)
    prefix = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + nums[i-1]
    for i in range(1, n+1):
        for j in range(i):
            m = max(m, prefix[i]-prefix[j])
    print(m)