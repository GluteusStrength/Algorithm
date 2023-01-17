import sys
n = int(input())
pos = []
for i in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    pos.append(l)
for x in range(n):
    import math
    x_1 = pos[x][0]
    y_1 = pos[x][1]
    x_2 = pos[x][3]
    y_2 = pos[x][4]
    r_1 = pos[x][2]
    r_2 = pos[x][5]
    dist_b = float(r_1 + r_2)
    dist_a = math.sqrt((x_1 - x_2) * (x_1 - x_2) + (y_1 - y_2) * (y_1 - y_2))
    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        print(-1)
    else:
        if x_1 == x_2 and y_1 == y_2 and r_1 != r_2:
            print(0)
        else:
            if r_1 < r_2:
                if dist_b == dist_a:
                    print(1)
                elif dist_b > dist_a:
                    if dist_a + r_1 == r_2:
                        print(1)
                    else:
                        if dist_a + r_1 < r_2:
                            print(0)
                        else:
                            print(2)
                else:
                    print(0)
            elif r_1 > r_2:
                if dist_b == dist_a:
                    print(1)
                elif dist_b > dist_a:
                    if dist_a + r_2 == r_1:
                        print(1)
                    else:
                        if dist_a + r_2 < r_1:
                            print(0)
                        else:
                            print(2)
                else:
                    print(0)
            else:
                if dist_a == dist_b:
                    print(1)
                elif dist_a > dist_b:
                    print(0)
                else:
                    print(2)
