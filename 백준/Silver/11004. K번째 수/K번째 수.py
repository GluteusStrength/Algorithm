import sys, heapq
n, k = map(int, input().split())
heap = []
nums = list(map(int, sys.stdin.readline().split()))
for i in nums:
    heapq.heappush(heap, i)
for j in range(k):
    if j != k - 1:
        heapq.heappop(heap)
    else:
        print(heapq.heappop(heap))
