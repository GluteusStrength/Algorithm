import sys
t = int(sys.stdin.readline())
l_0 = [1,0]
l_1 = [0,1]
for i in range(2, 41):
    l_0.append(l_0[i-2] + l_0[i-1])
    l_1.append(l_1[i-2] + l_1[i-1])
for _ in range(t):
    x = int(sys.stdin.readline())
    print(l_0[x], l_1[x])