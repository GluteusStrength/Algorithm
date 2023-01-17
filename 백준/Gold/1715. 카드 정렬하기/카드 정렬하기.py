import sys
import heapq # 힙 자료형으로 변환해서 생각한다.
n = int(input())
card = []
for i in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))
if len(card) == 1:
    print(0)
else:
    result = 0
    while True:
        num_1 = heapq.heappop(card)
        num_2 = heapq.heappop(card)
        s = num_1 + num_2
        result += s
        heapq.heappush(card, s)
        if len(card) == 1:
            break
    print(result)
