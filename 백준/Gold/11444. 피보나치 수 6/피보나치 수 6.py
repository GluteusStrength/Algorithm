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
                return mul(original, temp) # 원래꺼랑 나눈 거랑 해서 돌리기.

    matrix = div(original, n-1)
    print(matrix[0][0])
else:
    if n == 0:
        print(0)
    else:
        print(1)