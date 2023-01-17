import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
queue = deque([i for i in range(1, n+1)])
cnt = 0
for i in nums:
    if queue[0] == i:
        queue.popleft()
    else:
        idx = queue.index(i)
        if len(queue) - idx >= idx:
            cnt += idx
            for j in range(idx):
                x = queue.popleft()
                queue.append(x)
            queue.popleft()
        else:
            cnt += len(queue) - idx
            for j in range(len(queue) - idx):
                x = queue.pop()
                queue.appendleft(x)
            queue.popleft()
print(cnt)

