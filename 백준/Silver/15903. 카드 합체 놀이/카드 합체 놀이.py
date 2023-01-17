import sys, heapq
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
heapq.heapify(nums)
for _ in range(m):
    x = 0
    for _ in range(2):
        y = heapq.heappop(nums)
        x += y
    for _ in range(2):
        heapq.heappush(nums, x)
print(sum(nums))