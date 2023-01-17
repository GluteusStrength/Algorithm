from collections import deque
n, k = map(int, input().split())
MAX = 100000
visited = [-1 for _ in range(MAX+1)] # 그냥 0으로 초기화 시키고 not visited[i]라는 조건으로 걸어버리면 최소 방문으로 안 들어갈 수 있는 데이터도 있다.
q = deque()
q.append(n)
visited[n] = 0
def bfs(): # 가장 빠른, 짧은 내용의 문제 bfs 이용
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            return 0
        for i in (x-1, x+1, x*2):
            if i == x - 1 and (0 <= i and i <= MAX) and visited[i] == -1:
                q.append(i)
                visited[i] = visited[x] + 1
            if i == x * 2 and (0 < i and i <= MAX) and visited[i] == -1: # 얘가 x+1보다 우선순위가 돼야한다. 이유는 x == 1이면 x+1이나 x*2나 같다. 그래서 우선 순간이동으로 초기화해준다.
                visited[i] = visited[i//2]
                q.appendleft(i)
            if i == x + 1 and (0 <= i and i <= MAX) and visited[i] == -1:
                q.append(i)
                visited[i] = visited[x] + 1
bfs()

