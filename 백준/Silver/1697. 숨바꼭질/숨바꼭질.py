from collections import deque
n, k = map(int, input().split())
Max = 100001
location = [0 for _ in range(Max)]
q = deque()
q.append(n)
def bfs(): # 가장 빠른, 짧은 내용의 문제 bfs 이용
    while q:
        x = q.popleft()
        if x == k: # 해당 위치 도착 시 중단 후 방문 횟수 출력
            print(location[x])
            break
        else:
            for i in (x-1, x+1, 2*x): # deque이므로 tuple형
                if (0 <= i and i < Max) and not location[i]: # not location[i]의 조건이 들어간 이유는 해당 위치에 첫 방문 시 초기화 시키기 위해서 넣은 조건이다. 아니면 값이 달라질 수 있음
                    location[i] = location[x] + 1
                    q.append(i) # 새로운 위치 put
bfs()

