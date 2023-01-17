import sys, math
T = int(sys.stdin.readline())
def isprime(x):
    eratos = [1 for _ in range(x+1)]
    for i in range(2, int(math.sqrt(x))+1):
        if eratos[i] == 1:
            for j in range(i+i, x+1, i):
                eratos[j] = 0
    return [a for a in range(2, x+1) if eratos[a] == 1]
isp = isprime(1120)
dp = [[0 for _ in range(15)] for _ in range(1121)]
dp[0][0] = 1 # 그래야 일단 k == 1일때 소수의 경우를 1로 초기화 가능
for i in isp:
    for j in range(1120, 1, -1): # 중복을 생각하지 않기 위해서 역으로 내려온다.
        for k in range(1, 15):
            if j >= i:
                dp[j][k] += dp[j-i][k-1]
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a][b])
