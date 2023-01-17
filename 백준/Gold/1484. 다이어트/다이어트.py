import math
G = int(input())
present, past = 2, 1
res = []
while True:
    flag = math.pow(present, 2) - math.pow(past, 2)
    if present - past == 1:  # break 거는 조건
        if flag > G:
            break
    if flag == G:
        res.append(present)
        present += 1
    else:
        if flag < G:
            present += 1
        else:
            past += 1
if res:
    for i in res:
        print(i)
else:
    print(-1)
