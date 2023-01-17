n = int(input())
if n < 8:
    print(-1)
else:
    def isprime(n):
        eratos = [1] * 1000001
        for i in range(2, n+1):
            if eratos[i] == 1:
                for j in range(i+i, n+1, i):
                    eratos[j] = 0
        return [x for x in range(2, n+1) if eratos[x] == 1]
    def sum_isprime(k, l):
        isprime_l = isprime(k)
        prime_l = l
        for i in range(len(isprime_l)):
            for j in range(len(isprime_l) - 1, -1, -1):
                if isprime_l[i] + isprime_l[j] == k:
                    prime_l.append(isprime_l[i])
                    prime_l.append(isprime_l[j])
                    return prime_l
    if n % 2 == 0:
        if (n // 2) % 2 != 0:
            a = n // 2 - 1
            b = n // 2 + 1
            ans_l_1 = sum_isprime(a,[])
            ans_l_2 = sum_isprime(b,[])
            ans = ans_l_1 + ans_l_2
            ans.sort()
            print(*ans)
        else:
            a = n // 2
            ans_l = sum_isprime(a, [])
            ans_l += ans_l
            ans_l.sort()
            print(*ans_l)
    else:
        n_list = [2,3]
        x = n - sum(n_list)
        ans = n_list + sum_isprime(x,[])
        ans.sort()
        print(*ans)
