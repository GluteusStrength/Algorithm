import sys
l = list(map(int, sys.stdin.readline().split()))
new_l = []
a = l[0]
ans = 0
for i in range(5):
    new_l.append(a%10)
    a = a//10
for j in range(5):
    ans += (new_l[j]**5)
print(ans)