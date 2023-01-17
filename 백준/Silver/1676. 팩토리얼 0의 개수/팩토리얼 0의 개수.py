import math
n = int(input())
ans = str(math.factorial(n))
cnt = 0
for i in range(len(ans)-1, -1, -1):
    if ans[i] == '0':
        cnt += 1
    else:
        break
print(cnt)