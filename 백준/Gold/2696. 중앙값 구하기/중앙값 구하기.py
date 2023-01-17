import sys
import heapq
n = int(sys.stdin.readline())
for i in range(n):
    l_heap = []
    r_heap = []
    m = int(sys.stdin.readline())
    if m <= 10:
        nums = list(map(int, sys.stdin.readline().split()))
    else:
        div = m // 10
        nums = list(map(int, sys.stdin.readline().split()))
        for a in range(div):
            nums += list(map(int, sys.stdin.readline().split()))
    ans = []
    cnt = 0
    for j in nums:
        if len(l_heap) == len(r_heap):
            heapq.heappush(l_heap, -j)
        else:
            heapq.heappush(r_heap, j)
        if len(l_heap) >= 1 and len(r_heap) >= 1:
            if r_heap[0] < ((-1) * l_heap[0]):
                x = heapq.heappop(l_heap)
                y = heapq.heappop(r_heap)
                heapq.heappush(l_heap, -y)
                heapq.heappush(r_heap, -x)
        if len(l_heap) - len(r_heap) == 1:
            cnt += 1
            ans.append(-l_heap[0])
    print(cnt)
    if cnt <= 10:
        print(*ans)
    else:
        div = cnt // 10
        for x in range(div+1):
            if x != div:
                result = ans[10*x : 10*x+10]
                print(*result)
            else:
                result = ans[10*x:]
                print(*result)



