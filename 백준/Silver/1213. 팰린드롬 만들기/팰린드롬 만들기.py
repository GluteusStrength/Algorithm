word = input()
word_l = list(word)
l_set = list(set(word_l))
l_set.sort()
l = []
for i in l_set:
    l.append([i, word.count(i)])
if len(word) % 2 != 0:
    for i in l:
        if i[1] % 2 != 0:
            x = i
            l.remove(i)
            l.append(x)
cnt = 0
for i in l:
    if i[1] % 2 != 0:
        cnt += 1
if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    rpt = 0
    ans = ""
    cnt = 0
    if len(word) % 2 != 0:
        rpt += len(word) // 2 + 1
    else:
        rpt = len(word) // 2
    while True:
        cnt = 0
        for i in l:
            if i[1] % 2 == 0:
                ans += i[0] * (i[1] // 2)
                cnt += 1
        break
    if len(word) % 2 != 0:
        ans += l[-1][0] * (l[-1][1] // 2 + 1)
        ans = list(ans)
        ans_s = list(ans[:-1])
        ans_s.sort()
        ans_s.append(ans[-1])
        ans_front = "".join(ans_s)
        ans_back = list("".join(ans_s)[::-1])
        ans_back.remove(ans_back[0])
        ans_back = "".join(ans_back)
        print(ans_front+ans_back)
    else:
        ans += ans[::-1]
        print(ans)
