s = input()
p = input()
if p[0] not in s:
    print(0)
else:
    cnt = 0
    j = 0
    pi = [0 for _ in range(len(p))]
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    k = 0
    for i in range(len(s)):
        while k > 0 and p[k] != s[i]:
            k = pi[k-1]
        if p[k] == s[i]:
            if k == (len(p) - 1):
                cnt += 1
            else:
                k += 1
        if cnt == 1:
            break
    print(cnt)
