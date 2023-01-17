T = input()
t = int(T)
if t == 1 :
    print(10)
else:
    up_list = [[0]*10 for i in range(t+1)]
    for x in range(t+1):
        for y in range(10):
            if x == 0:
                up_list[x][y] = 1
            else:
                up_list[x][0] = 1
    for a in range(1, t+1):
        for b in range(10):
            up_list[a][b] = up_list[a-1][b] + up_list[a][b-1]
    print(up_list[t][9] % 10007)