import sys
n = int(input())
def eratos(n):
    n += 1
    isprime = [1] * (n)
    for i in range(3, n):
        if isprime[i] == 1:
            for j in range(i+i, n, i):
                isprime[j] = 0
    return [i for i in range(2, n) if isprime[i] == 1]
isprime_l = eratos(32000)
for x in range(n):
    n = int(sys.stdin.readline())
    if n == 4:
        print("4 has 1 representation(s)\n2+2\n")
    else:
        cnt = 0
        l = []
        for a in range(3, n//2 + 1, 2):
            if a in isprime_l and n-a in isprime_l:
                l.append((a, n-a))
                cnt += 1
        print(str(n) + " has "+ str(cnt) + " representation(s)")
        for b in range(cnt):
            if b != cnt - 1:
                print("{}+{}".format(l[b][0], l[b][1]))
            else:
                print("{}+{}\n".format(l[b][0], l[b][1]))


