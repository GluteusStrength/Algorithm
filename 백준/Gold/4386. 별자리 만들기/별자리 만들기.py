import sys, math
n = int(input())
star = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
distance_set = []
for i in range(n-1):
    for j in range(i+1, n):
        d = math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)
        distance_set.append([d, i, j])
distance_set.sort(key = lambda x : x[0]) # 오름차순으로 정렬
root = [i for i in range(n+1)]
def find(x):
    if root[x] == x:
        return x
    return find(root[x])
res = 0
for d, i, j in distance_set:
    if find(i) != find(j):
        a = find(i)
        b = find(j)
        root[b] = a
        res += d
print(round(res, 2))