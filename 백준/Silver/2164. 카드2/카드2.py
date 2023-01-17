from collections import deque
n = int(input())
card = deque()
for i in range(1, n+1):
    card.append(i)
for _ in range(n-1):
    card.popleft()
    x = card.popleft()
    card.append(x)
print(card[0])