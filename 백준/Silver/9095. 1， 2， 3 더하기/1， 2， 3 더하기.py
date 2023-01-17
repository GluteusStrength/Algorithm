import math
N = input()
n = int(N)
f = []
for x in range(n):
    y = input()
    f.append(int(y))
cnt = 0
ans = []
for i in range(n):
    r = f[i]
    max_c = r // 3
    while max_c >= 0:
        k = r - 3*max_c
        for a in range(k+1):
            for b in range(k+1):
                if a + 2*b == k:
                    ans.append((a,b,max_c))
        max_c -= 1
    for q in range(len(ans)):
        comb = ans[q]
        a = comb[0]
        b = comb[1]
        c = comb[2]
        if comb.count(0) == 2:
            cnt += 1
        else:
            x = math.factorial(a + b + c)
            f_abc = math.factorial(a) * math.factorial(b) * math.factorial(c)
            h = int(x / f_abc)
            cnt += h
    print(cnt)
    ans = []
    cnt = 0


