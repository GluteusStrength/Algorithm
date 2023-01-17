import sys
import heapq
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    x.sort()
    l.append(x)
d = int(sys.stdin.readline())
l.sort(key = lambda x : x[1]) # 항상 오른쪽이 기준! 따라서 뒤에 값에 따라서 정렬
q = []
ans = 0
for i in l:
    if i[1] - i[0] > d:
        pass
    else:
        if not q:
            heapq.heappush(q, i)
            ans = len(q)
        else:
            while i[1] - q[0][0] > d:
                heapq.heappop(q)
                if not q:
                    break
            heapq.heappush(q, i)
            ans = max(len(q), ans)
print(ans)


