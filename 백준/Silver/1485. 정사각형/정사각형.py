import sys
import math
n = int(input())
for i in range(n):
    area = []
    for j in range(4):
        area.append(list(map(int, sys.stdin.readline().split())))
    area.sort()
    x_1 = area[0]
    x_2 = area[1]
    x_3 = area[2]
    x_4 = area[3]
    cross_1 = math.pow((x_4[0] - x_1[0]), 2) + math.pow((x_4[1] - x_1[1]), 2)
    cross_2 = math.pow((x_3[0] - x_2[0]), 2) + math.pow((x_3[1] - x_2[1]), 2)
    l_1 = math.pow((x_2[0] - x_1[0]), 2) + math.pow((x_2[1] - x_1[1]), 2)
    l_2 = math.pow((x_3[0] - x_1[0]), 2) + math.pow((x_3[1] - x_1[1]), 2)
    l_3 = math.pow((x_4[0] - x_3[0]), 2) + math.pow((x_4[1] - x_3[1]), 2)
    l_4 = math.pow((x_4[0] - x_2[0]), 2) + math.pow((x_4[1] - x_2[1]), 2)
    if l_1 == l_2 == l_3 == l_4:
        if cross_1 == cross_2:
            print(1)
        else:
            print(0)
    else:
        print(0)
