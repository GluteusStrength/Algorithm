import sys
import heapq
k, n = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
heap = []

for i in nums:
    heapq.heappush(heap, i)
for x in range(n):
    head = heapq.heappop(heap)
    for y in range(k):
        num = nums[y] * head
        heapq.heappush(heap, num)
        if head % nums[y] == 0:
            # 먼저 앞에서 2*2 / 3*2,3 / 5*2,3,5 이런식으로 선빵 쳐서 중복을 끊어버린다.
            break
print(head)