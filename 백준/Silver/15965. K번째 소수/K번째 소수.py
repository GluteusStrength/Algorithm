k = int(input())
#에라토스테네스의 체를 이용한다.
def eratos(n):
    l = [1 for _ in range(n)]
    for i in range(2, n):
        if l[i] == 1:
            for j in range(i+i, n, i):
                l[j] = 0
    return [x for x in range(2, n) if l[x] == 1]

x = eratos(500001)
print(x[k-1])