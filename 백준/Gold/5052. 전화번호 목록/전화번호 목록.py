import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    p = [sys.stdin.readline().rstrip() for _ in range(n)]
    flag = True
    p.sort()
    for j in range(n-1): # 연쇄적으로 이어져도 된다. 왜냐하면 어차피 접두어만 비교하기 때문이다.
        if p[j] == p[j+1][:len(p[j])]:
            flag = False
            break
    if flag == False:
        print('NO')
    else:
        print("YES")

