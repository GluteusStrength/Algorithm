from collections import deque
s = int(input())
dp = [[0 for _ in range(s+1)] for _ in range(s+1)]
q = deque()
q.append((1,0))
while q:
    x, y = q.popleft()
    if dp[x][x] == 0: # 이모티콘을 복사해서 클립보드에 저장
        dp[x][x] = dp[x][y]+1
        q.append((x,x))
    if x+y <= s and dp[x+y][y] == 0: # 클립보드의 모든 이모티콘을 화면에 붙여넣기
        dp[x+y][y] = dp[x][y]+1
        q.append((x+y, y))
    if x-1 >= 0 and dp[x-1][y] == 0: # 화면의 이모티콘 중 하나를 삭제
        dp[x-1][y] = dp[x][y]+1
        q.append((x-1, y))
print(min(dp[s][1:]))
