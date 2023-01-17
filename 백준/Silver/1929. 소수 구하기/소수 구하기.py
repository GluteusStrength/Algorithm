a,b = input().split()
a = int(a)
b = int(b)
def eratos(x):
    if x % 2 == 0 and x != 2:
        return False
    if x == 2 or x == 3 or x == 5 or x == 7:
        return True
    for i in range(3, int(x**0.5+1)):
        if x % i == 0:
            return False
        else:
            if (x % i != 0) and (i != int(x**0.5)):
                continue
            else:
                return True
for x in range(a,b+1):
    if eratos(x) == True:
        print(x)
