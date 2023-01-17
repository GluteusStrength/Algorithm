import sys
import heapq

n = int(sys.stdin.readline())

heap = []
computers = [0 for _ in range(n)]
count = [0 for _ in range(n)]

su = 0

for _ in range(n):
    p,q = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, [p,q])

while heap:
    temp = heapq.heappop(heap)
    for i in range(len(computers)):
        if computers[i] <= temp[0]:
            if computers[i] == 0:
                su += 1
            computers[i] = temp[1]
            count[i] += 1
            break

print(su)

for i in count:
    if i == 0:
        pass
    else:
        print(i, end= " ")