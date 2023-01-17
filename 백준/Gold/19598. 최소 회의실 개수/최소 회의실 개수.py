import sys # ?? tlqkf 왜 시작시간 오름차순은 되는데 종료시간은 안 되냐 ?
import heapq
n = int(sys.stdin.readline())
m = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
m.sort(key = lambda x : x[0])
heap = []
while m:
    if not heap:
        x = heapq.heappop(m)
        heapq.heappush(heap, x[1])
    else:
        x = heapq.heappop(m)
        if x[0] < heap[0]:
            heapq.heappush(heap, x[1])
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, x[1])
print(len(heap))