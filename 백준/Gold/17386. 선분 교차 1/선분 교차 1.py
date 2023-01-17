import sys
l_1 = list(map(int, sys.stdin.readline().split()))
l_2 = list(map(int, sys.stdin.readline().split()))
A = (l_1[0], l_1[1])
B = (l_1[2], l_1[3])
C = (l_2[0], l_2[1])
D = (l_2[2], l_2[3])
def ccw(x,y,z,ans): # 벡터의 외적
    v_1 = (y[0] - x[0], y[1] - x[1])
    v_2 = (z[0] - x[0], z[1] - x[1])
    cross_p = v_1[0]*v_2[1] - v_1[1]*v_2[0]
    if cross_p > 0:
        return ans
    else:
        return ans * -1
if ccw(A,B,C,1)*ccw(A,B,D,1) < 0 and ccw(C,D,A,1) * ccw(C,D,B,1) < 0:
    print(1)
else:
    print(0)
