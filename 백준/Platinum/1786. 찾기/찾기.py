import sys
t = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
table = [0 for _ in range(len(p))]
j = 0
for i in range(1, len(table)):
    while j > 0 and p[i] != p[j]:
        j = table[j-1]
    if p[i] == p[j]:
        j += 1
        table[i] = j
cnt = 0
ans = []
j = 0
for i in range(len(t)):
    while j > 0 and t[i] != p[j]:
        j = table[j-1]
    if t[i] == p[j]:
        if j == (len(p) - 1):
            cnt += 1
            ans.append(i-len(p)+2)
            j = table[j]
        else:
            j += 1
print(cnt)
print(*ans)

