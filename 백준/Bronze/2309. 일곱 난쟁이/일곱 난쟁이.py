from itertools import combinations
l = [int(input()) for _ in range(9)]
nums = [i for i in range(9)]
l.sort()
x = combinations(nums, 7)
flag = False
for i in x:
    s = 0
    for j in i:
        s+=l[j]
        if s == 100:
            flag = True
            for k in i:
                print(l[k])
    if flag == True:
        break
