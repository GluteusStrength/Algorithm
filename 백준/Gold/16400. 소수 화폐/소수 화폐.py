import sys
n = int(sys.stdin.readline())
def isprime(x):
    eratos = [1 for _ in range(x+1)]
    for i in range(2, x+1):
        if eratos[i] == 1:
            for j in range(i+i, x+1, i):
                eratos[j] = 0
    return [a for a in range(2, x+1) if eratos[a] == 1]
dp = [0 for _ in range(n+1)]
isp_list = isprime(n)
for i in isp_list:
    if i == isp_list:
        for j in range(i, n+1, i):
            dp[j] = 1
    else:
        for j in range(i, n+1):
            if i == j:
                dp[j] += 1
            else:
                dp[j] = (dp[j] + dp[j-i]) % 123456789
print(dp[n])
