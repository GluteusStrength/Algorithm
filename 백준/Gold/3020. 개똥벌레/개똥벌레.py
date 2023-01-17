import sys
n, h = map(int, sys.stdin.readline().split())
top = [0 for _ in range(h+1)] # 종유석
bottom = [0 for _ in range(h+1)] # 석순
result = [0 for _ in range(h+1)]
for i in range(1, n+1):
    if i % 2 != 0:
        bottom[h - int(sys.stdin.readline()) + 1] += 1
    else:
        top[int(sys.stdin.readline())] += 1
for i in range(h-1, 0, -1):
    top[i] += top[i+1]
for i in range(1, h+1):
    bottom[i] += bottom[i-1]
for i in range(1, h+1):
    result[i] = top[i] + bottom[i]
ans = result[1:]
x = min(ans)
print(x, ans.count(x))


