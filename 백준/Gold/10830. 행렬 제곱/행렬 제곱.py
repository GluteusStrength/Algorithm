import sys
n, b = map(int, sys.stdin.readline().split())
o_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 행렬의 제곱을 내는 함수.
def mul(m_1, m_2):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat[i][j] += m_1[i][k] * m_2[k][j]
            mat[i][j] %= 1000
    return mat

# 분할
def div(ma, b):
    if b == 1:
        return ma
    else:
        if b % 2 == 0:
            m = div(ma, b//2)
            return mul(m, m)
        else:
            temp = div(ma, b - 1)
            return mul(o_matrix, temp) # 원래꺼랑 나눈 거랑 해서 돌리기.

ans = div(o_matrix, b)
for i in ans:
    for j in i:
        print(j % 1000, end = ' ')
    print()
