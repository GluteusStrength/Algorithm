#직접 나눠서 해야하는 문제
import sys
n, m = map(int, sys.stdin.readline().split())
matrix = [[0 for _ in range(m+1)]]
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    s = list(s)
    l = [0]
    for i in s:
        l.append(int(i))
    matrix.append(l)
# 각 누적합 구하기
psum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        psum[i][j] = psum[i-1][j] + psum[i][j-1] + matrix[i][j] - psum[i-1][j-1]

ans = 0

#이는 쪼갰을 때 쪼갠 부위의 숫자의 합을 return한다. (a,b)는 start이고 (c,d)는 end라고 생각한다.
def selection(a,b,c,d):
    return psum[c][d] - psum[c][b-1] - psum[a-1][d] + psum[a-1][b-1]

#총 6가지의 case // start와 end를 잘 생각한다.

#case 1(세로로만)
for i in range(1, m-1):
    for j in range(i+1, m):
        l_1 = selection(1, 1, n, i)
        l_2 = selection(1, i+1, n, j)
        l_3 = selection(1, j+1, n, m)
        ans = max(ans, l_1*l_2*l_3)

#case 2(가로로만)
for i in range(1, n-1):
    for j in range(i+1, n):
        l_1 = selection(1, 1, i, m)
        l_2 = selection(i+1, 1, j, m)
        l_3 = selection(j+1, 1, n, m)
        ans = max(ans, l_1*l_2*l_3)

#case 3(ㅓ)
for i in range(1, n):
    for j in range(1, m):
        l_1 = selection(1, 1, i, j)
        l_2 = selection(i+1, 1, n, j)
        l_3 = selection(1, j+1, n, m)
        ans = max(ans, l_1*l_2*l_3)

#case 4(ㅏ)
for i in range(2, n):
    for j in range(2, m):
        l_1 = selection(1, 1, n, j-1)
        l_2 = selection(1, j, i, m)
        l_3 = selection(i+1, j, n, m)
        ans = max(ans, l_1*l_2*l_3)

#case 5(ㅜ)
for i in range(1, n):
    for j in range(1, m):
        l_1 = selection(1, 1, i, m)
        l_2 = selection(i+1, 1, n, j)
        l_3 = selection(i+1, j+1, n, m)
        ans = max(ans, l_1*l_2*l_3)

#case 6(ㅗ)
for i in range(1, n):
    for j in range(1, m):
        l_1 = selection(1, 1, i, j)
        l_2 = selection(1, j+1, i, m)
        l_3 = selection(i+1, 1, n, m)
        ans = max(ans, l_1*l_2*l_3)
print(ans)