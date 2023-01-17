t = int(input())
for i in range(t):
    w = input()
    k = int(input())
    word_l = list(w)
    w_l = list(set(word_l))
    w_d = dict()
    if k == 1:
        print(1, 1)
    else:
        for j in w_l:
            ind = []
            if w.count(j) >= k:
                for a in range(len(w)):
                    if w[a] == j:
                        ind.append(a)
                w_d[j] = ind
        if w_d:
            cnt = k
            cnt -= 1
            d = []
            ans = []
            for x in w_d:
                ind = w_d[x]
                for y in range(len(ind)):
                    for z in range(y):
                        if y - z == k - 1:
                            d.append(ind[y] - ind[z] + 1)
            ans.append(min(d))
            ans.append(max(d))
            print(*ans)
        else:
            print(-1)

