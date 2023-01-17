import sys
from itertools import combinations # 이 툴을 쓰면 간단하다
l, c = map(int, sys.stdin.readline().split())
word = list(map(str, sys.stdin.readline().split()))
word.sort()
comb_l = []
for i in range(c):
    comb_l.append(i)
group = list(combinations(comb_l, l))
pos_word = []
for j in group:
    s = ""
    for k in j:
        s += word[k]
    pos_word.append(s)
for x in pos_word:
    a = x.count('a') + x.count('e') + x.count('i') + x.count("o") + x.count('u')
    if a >= 1:
        if len(x) - a >= 2:
            print(x)
    else:
        continue
