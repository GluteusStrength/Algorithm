import sys
import heapq

n = int(sys.stdin.readline())
c = []
for _ in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))
c.sort(key = lambda x : x[0]) # 우선 시작을 기준으로 오름차순 정렬
c.sort(key = lambda x : x[1]) # 그 후 끝을 기준으로 정렬
cnt, end = 0, 0
for s, e in c:
    if s >= end:
        cnt += 1
        end = e
print(cnt)

