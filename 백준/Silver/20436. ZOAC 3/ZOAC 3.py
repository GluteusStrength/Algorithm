import sys
import math
a, b = map(str, sys.stdin.readline().split())
w = input()
left = [['q','w','e','r','t'], ['a','s','d','f','g'], ['z','x','c','v']]
right = [['y','u','i','o','p'], ['h','j','k','l'], ['b','n','m']]
ja = "qwertasdfgzxcv"
mo = "yuiophjklbnm"
m = -1
n = -1
o = -1
p = -1
for i in range(3):
    for j in range(len(left[i])):
        if a == left[i][j]:
            m = i
            n = j
            break
    if m != -1 and n != -1:
        break
for i in range(3):
    for j in range(len(right[i])):
        if b == right[i][j]:
            o = i
            p = j + len(left[i])
            break
    if o != -1 and p != -1:
        break
result = 0
for i in w:
    s = i
    ind_1 = -1
    ind_2 = -1
    ind_3 = -1
    ind_4 = -1
    result += 1
    if s in ja:
        for j in range(3):
            for k in range(len(left[j])):
                if s == left[j][k]:
                    ind_1 = j
                    ind_2 = k
                    break
            if ind_1 != -1 and ind_2 != -1:
                break
        result += int(math.fabs(m - ind_1) + math.fabs(n - ind_2))
        m = ind_1
        n = ind_2
    else:
        for x in range(3):
            for y in range(len(right[x])):
                if s == right[x][y]:
                    ind_3 = x
                    ind_4 = y + len(left[x])
                    break
            if ind_3 != -1 and ind_4 != -1:
                break
        result += int(math.fabs(o - ind_3) + math.fabs(p - ind_4))
        o = ind_3
        p = ind_4
print(result)
