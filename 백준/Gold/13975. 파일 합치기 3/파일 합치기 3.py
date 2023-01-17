import sys
import heapq # 작은 순서대로 파일을 합쳐야 최소비용이 나오기 때문에 최소 큐를 이용
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    file = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(file)
    r = 0
    while len(file) > 1: 
        x = heapq.heappop(file)
        y = heapq.heappop(file)
        r += (x+y)
        heapq.heappush(file, x+y)
    print(r)