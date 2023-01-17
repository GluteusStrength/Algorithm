import sys
n = int(sys.stdin.readline())
original = [[1, 1], [1, 0]]
# 행렬의 제곱을 내는 함수.
if n >= 2:
    def mul(m_1, m_2):
        mat = [[0 for _ in range(2)] for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    mat[i][j] += m_1[i][k] * m_2[k][j]
                mat[i][j] %= 1000000007
        return mat

    # 분할
    def div(o, n):
        if n == 1:
            return o
        else:
            if n % 2 == 0:
                m = div(o, n//2)
                return mul(m, m)
            else:
                temp = div(o, n-1)
                return mul(original, temp)
    if n % 2 == 0:
        ans = div(original, n)
        ans = ans[0][0] % 10000000007 # 규칙이 있다. f(2n + 1) - 1 = sum(f(2n))이다.
        print(ans - 1)
    else:
        ans = div(original, n-1)
        ans = ans[0][0] % 1000000007
        print(ans - 1)
else:
    print(0)