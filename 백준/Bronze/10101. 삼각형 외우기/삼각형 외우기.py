angle = [int(input()) for _ in range(3)]
if sum(angle) != 180:
    print("Error")
else:
    flag = True
    for i in angle:
        if i != 60:
            flag = False
    if flag:
        print("Equilateral")
    else:
        f = False
        for j in angle:
            if angle.count(j) == 2:
                f = True
                break
        if f:
            print("Isosceles")
        else:
            print("Scalene")