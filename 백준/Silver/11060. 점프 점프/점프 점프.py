import sys
n = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))
last = len(box) - 1
def find(e, l, ind_l):
    ind = e-1
    f_ind = []
    ind_diff = 1
    temp = -1
    for x in range(ind, -1, -1):
        if l[x] >= ind_diff:
            f_ind.append(l[x])
            ind_diff += 1
            temp = x
        else:
            ind_diff += 1
    if temp == -1:
        return -1
    else:
        ind = temp
        if ind == 0:
            ind_l.append(f_ind[-1])
            return ind_l
        else:
            ind_l.append(f_ind[-1])
            return find(ind, box, ind_l)
a = find(last, box, [])
if n == 1:
    print(0)
else:
    if a == -1:
        print(a)
    else:
        print(len(a))
