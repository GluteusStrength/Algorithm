import sys
a = int(input())
data = []
for i in range(a):
    l = list(map(int, sys.stdin.readline().split()))
    data.append(l)
for j in range(len(data)):
    f = data[j]
    h = f[0]
    w = f[1]
    n = f[2]
    if h*w < n:
        break
    else:
        house = []
        a = 1
        b = 0
        x = n // h
        y = n % h
        if y != 0:
            a += x
            b += y
            house.append(b)
            house.append(a)
            for i in range(2):
                house[0] = str(house[0])
                if i == 1:
                    if house[1] < 10:
                        house[1] = "0"+str(house[1])
                    else:
                        house[1] = str(house[1])
            print(int("".join(house)))
        else:
            house.append(h) #무조건 꼭대기 층
            b += x
            house.append(b)
            for i in range(2):
                house[0] = str(house[0])
                if i == 1:
                    if house[1] < 10:
                        house[1] = "0" + str(house[1])
                    else:
                        house[1] = str(house[1])
            print(int("".join(house)))