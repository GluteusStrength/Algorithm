import sys
l_1 = list(map(int, sys.stdin.readline().split()))
l_2 = list(map(int, sys.stdin.readline().split()))
A = (l_1[0], l_1[1])
B = (l_1[2], l_1[3])
C = (l_2[0], l_2[1])
D = (l_2[2], l_2[3])
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
        x = min(C[0], D[0])
        w = max(C[0], D[0])
        y = min(A[0], B[0])
        z = max(A[0], B[0])
        if x in range(y,z+1):
            if A[0] - B[0] != 0:
                print(1)
            else:
                a = min(C[1], D[1])
                b = max(C[1], D[1])
                c = min(A[1], B[1])
                d = max(A[1], B[1])
                if a in range(c, d+1):
                    print(1)
                elif b in range(c, d+1):
                    print(1)
                elif a <= c and b >= d:
                    print(1)
                else:
                    print(0)
        elif w in range(y,z+1):
            if A[0] - B[0] != 0:
                print(1)
            else:
                a = min(C[1], D[1])
                b = max(C[1], D[1])
                c = min(A[1], B[1])
                d = max(A[1], B[1])
                if a in range(c, d+1):
                    print(1)
                elif b in range(c, d+1):
                    print(1)
                elif a <= c and b >= d:
                    print(1)
                else:
                    print(0)
        elif x <= y and w >= z:
            if A[0] - B[0] != 0:
                print(1)
            else:
                a = min(C[1], D[1])
                b = max(C[1], D[1])
                c = min(A[1], B[1])
                d = max(A[1], B[1])
                if a in range(c, d+1):
                    print(1)
                elif b in range(c, d+1):
                    print(1)
                elif a <= c and b >= d:
                    print(1)
                else:
                    print(0)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
