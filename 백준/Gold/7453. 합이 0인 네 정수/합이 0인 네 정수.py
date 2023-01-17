import sys
n = int(sys.stdin.readline())
nums = [[] for _ in range(4)]
A,B,C,D = [], [], [], []
for _ in range(n):
    a,b,c,d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
a_b_sum = dict()
for a in A: # a+b가 -c-d와 같으면 됨. 다른 케이스는 상관 없는 게 어차피 a+b+c+d = 0 이기 때문이다
    for b in B:
        if not a_b_sum.get(a+b):
            a_b_sum[a+b] = 1
        else:
            a_b_sum[a+b] += 1
ans = 0
for c in C:
    for d in D:
        if -c-d in a_b_sum.keys():
            ans += a_b_sum[-c-d]
print(ans)