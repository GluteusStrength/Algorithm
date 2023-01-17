import sys
import heapq
n = int(sys.stdin.readline())
if n == 0:
    print(0)
else:
    univ = []
    for i in range(n):
        univ.append(list(map(int, sys.stdin.readline().split())))
    univ = sorted(univ, key = lambda x : (x[1], x[0]))
    min_date = univ[0][1]
    if min_date >= n:
        result = 0
        for i in univ:
            result += i[0]
        print(result)
    else:
        payment = []
        for i in univ:
            heapq.heappush(payment, i[0])
            if len(payment) > i[1]:
                heapq.heappop(payment)
        print(sum(payment))
