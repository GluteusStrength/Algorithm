from collections import defaultdict
w = input()
cnt = 0
dic = defaultdict(int)
for i in w:
    if ord(i) >= 97:
        change = ord(i) - 32
        change = chr(change)
        dic[change] += 1
    else:
        dic[i] += 1
x = list(dic.values())
if x.count(max(x)) >= 2:
    print("?")
else:
    flag = max(x)
    for i in dic:
        if dic[i] == flag:
            print(i)
            break
