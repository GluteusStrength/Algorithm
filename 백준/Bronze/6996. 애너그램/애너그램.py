n = int(input())
import sys
l = []
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    l.append([a,b])
for j in range(n):
    w_1 = list(l[j][0])
    w_2 = list(l[j][1])
    w_1.sort()
    w_2.sort()
    if w_1 == w_2:
        f_w_1 = l[j][0]
        f_w_2 = l[j][1]
        print('{} & {} are anagrams.'.format(f_w_1, f_w_2))
    else:
        f_w_1 = l[j][0]
        f_w_2 = l[j][1]
        print('{} & {} are NOT anagrams.'.format(f_w_1, f_w_2))