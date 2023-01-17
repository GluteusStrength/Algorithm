T = input()
l = list()
r = 0
while r < int(T) :
    x , y = input().split()
    n_1 = int(x)
    n_2 = int(y)
    if (n_1 >= 1 and n_1 <=100) and (n_2 >= 1 and n_2 <= 1000000):
        if (n_1 % 10) == 1 :
            print(1)
            r += 1
        elif (n_1 % 10) == 2 :
            r_2 = [2, 4, 8, 6]
            print(r_2[(n_2%4) - 1])
            r += 1
        elif (n_1 % 10) == 3:
            r_3 = [3, 9, 7, 1]
            print(r_3[(n_2%4) - 1])
            r += 1
        elif (n_1 % 10) == 4:
            r_4 = [4, 6]
            print(r_4[(n_2%2) - 1])
            r += 1
        elif (n_1 % 10) == 5 :
            print(5)
            r+=1
        elif (n_1 % 10) == 6 :
            print(6)
            r+=1
        elif (n_1 % 10) == 7 :
            r_7 = [7, 9, 3, 1]
            print(r_7[(n_2%4) - 1])
            r += 1
        elif (n_1 % 10) == 8 :
            r_8 = [8, 4, 2, 6]
            print(r_8[(n_2 % 4) - 1])
            r+=1
        elif (n_1 % 10) == 9 :
            r_9 = [9, 1]
            print(r_9[(n_2 % 2) - 1])
            r+=1
        else:
            print(10)
            r+=1
    else:
        if n_2 == 0 :
            print(1)
            r+=1



