import sys, heapq
n = int(input())
heap = []
ans = 0
prob = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
heapq.heapify(prob)
for i in range(n):
    dead, cup = heapq.heappop(prob)
    heapq.heappush(heap, cup)
    while dead < len(heap):
        heapq.heappop(heap)
print(sum(heap))