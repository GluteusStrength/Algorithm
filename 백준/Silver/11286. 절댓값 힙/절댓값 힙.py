import sys
import heapq
n = int(input())
heap_p = []
heap_m = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        if x > 0:
            heapq.heappush(heap_p, x)
        else:
            heapq.heappush(heap_m, -x)
    else:
        if not heap_p and not heap_m:
            print(0)
        else:
            if not heap_p and heap_m:
                a = heapq.heappop(heap_m)
                print(-a)
            elif heap_p and not heap_m:
                print(heapq.heappop(heap_p))
            else:
                a = heap_m[0]
                b = heap_p[0]
                if a <= b:
                    a = heapq.heappop(heap_m)
                    print(-a)
                else:
                    print(heapq.heappop(heap_p))

