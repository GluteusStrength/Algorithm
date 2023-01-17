import sys
l = []
for i in range(3):
    l.append(list(map(int, sys.stdin.readline().split())))
A = l[0]
B = l[1]
C = l[2]
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
print(ccw(A,B,C,1))
