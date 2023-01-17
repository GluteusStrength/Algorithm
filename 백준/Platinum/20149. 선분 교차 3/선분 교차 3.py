import sys
l_1 = list(map(int, sys.stdin.readline().split()))
l_2 = list(map(int, sys.stdin.readline().split()))
A = (l_1[0], l_1[1])
B = (l_1[2], l_1[3])
C = (l_2[0], l_2[1])
D = (l_2[2], l_2[3])
l_1 = [A,B]
l_2 = [C,D]
def ccw(x,y,z,ans): # 벡터의 외적 , ccw문제는 cross product이다.
    v_1 = (y[0] - x[0], y[1] - x[1])
    v_2 = (z[0] - x[0], z[1] - x[1])
    cross_p = v_1[0]*v_2[1] - v_1[1]*v_2[0]
    if cross_p > 0:
        return ans
    elif cross_p == 0:
        return 0
    else:
        return ans * -1
if ccw(A,B,C,1)*ccw(A,B,D,1) <= 0 and ccw(C,D,A,1) * ccw(C,D,B,1) <= 0:
    if ccw(A,B,C,1) == 0 and ccw(A,B,D,1) == 0 and ccw(C,D,A,1) == 0 and ccw(C,D,B,1) == 0:
        if A[0] - B[0] == 0:
            x = min(C[1], D[1])
            y = max(C[1], D[1])
            z = min(A[1], B[1])
            w = max(A[1], B[1])
            if x == w and y > w:
                print(1)
                for i in l_2:
                    if i in l_1:
                        print(*i)
            elif y == z and x < z:
                print(1)
                for i in l_2:
                    if i in l_1:
                        print(*i)
            elif x in range(z, w+1) and y in range(z, w+1):
                print(1)
            elif x in range(z,w) or y in range(z,w):
                print(1)
            elif x <= z and y >= w:
                print(1)
            else:
                print(0)
        elif A[1] - B[1] == 0:
            x = min(C[0], D[0])
            y = max(C[0], D[0])
            z = min(A[0], B[0])
            w = max(A[0], B[0])
            if x == w and y > w:
                print(1)
                for i in l_2:
                    if i in l_1:
                        print(*i)
            elif y == z and x < z:
                print(1)
                for i in l_2:
                    if i in l_1:
                        print(*i)
            elif x in range(z, w + 1) and y in range(z, w + 1):
                print(1)
            elif x in range(z, w) or y in range(z, w):
                print(1)
            elif x <= z and y >= w:
                print(1)
            else:
                print(0)
        else:
            x = min(C[0], D[0])
            y = max(C[0], D[0])
            z = min(A[0], B[0])
            w = max(A[0], B[0])
            if x == w and y > w:
                print(1)
                for i in l_2:
                    if i in l_1:
                        print(*i)
            elif y == z and x < z:
                print(1)
                for i in l_2:
                    if i in l_1:
                        print(*i)
            elif x in range(z, w + 1) and y in range(z, w + 1):
                print(1)
            elif x in range(z, w) or y in range(z, w):
                print(1)
            elif x <= z and y >= w:
                print(1)
            else:
                print(0)
    else:
        print(1)
        x = float('inf')
        y = float('inf')
        if D[0] - C[0] != 0 and B[0] - A[0] != 0:
            a = (D[1] - C[1]) / (D[0] - C[0])
            b = (B[1] - A[1]) / (B[0] - A[0])
            x = (a * C[0] - b * A[0] + A[1] - C[1]) / (a - b)
            y = b * x + A[1] - b * A[0]
            if x == int(x) and y == int(y):
                print(int(x), int(y))
            else:
                if x == int(x) and y != int(y):
                    print(int(x), y)
                elif x != int(x) and y == int(y):
                    print(x, int(y))
                else:
                    print(x,y)
        if D[0] - C[0] == 0 and B[0] - A[0] != 0:
            x = D[0]
            y = ((B[1] - A[1]) / (B[0] - A[0])) * (x - A[0]) + A[1]
            if y == int(y):
                y = int(y)
            print(x,y)
        if B[0] - A[0] == 0 and D[0] - C[0] != 0:
            x = B[0]
            y = ((D[1] - C[1]) / (D[0] - C[0])) * (x - C[0]) + C[1]
            if y == int(y):
                y = int(y)
            print(x,y)
        if x == float("inf") and y == float('inf'):
            for i in l_2:
                if i in l_1:
                    print(*i)
            if A[0] - B[0] == 0 and C[1] - D[1] == 0:
                print(A[0], C[1])
            if A[1] - B[1] == 0 and C[0] - D[0] == 0:
                print(C[0], A[1])
else:
    print(0)
