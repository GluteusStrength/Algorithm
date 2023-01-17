from collections import deque
n, k = map(int, input().split())
Max = 100000
location = [-1 for _ in range(Max+1)]
q = deque()
q.append(n)
location[n] = 0
def bfs(way):
    while q:
        x = q.popleft()
        if x == k: # 해당 위치 도착 시 중단 후 방문 횟수 출력. q에 들어간 것은 따지고 보면 최소로 도달한 방법으로만을 기록한 것이다.
            way += 1 # 방법은 그냥 이렇게 가도 되긴한다.
        else:
            for i in (x-1, x+1, 2*x):
                if (0 <= i and i <= Max) and (location[i] == -1):
                    location[i] = location[x] + 1
                    q.append(i) # 새로운 위치 put
                elif (0 <= i and i <= Max) and (location[i] == location[x] + 1): # 이 조건이 필요한 이유: 첫 방문은 아니지만 이 때까지 온 새로운 방법을 기록하기 위해 -> 큐에 넣는다 이런경우도
                    q.append(i)
    return location[k], way
ans = bfs(0)
print(ans[0])
print(ans[1])


