n = int(input())
l = []
for i in range(n):
    x = input()
    l.append(list(x))
def div(x,y,n):
    result = ""
    standard = True
    s = l[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if s != l[i][j]:
                standard = False
                break
    if standard:
        if l[x][y] == "1":
            result += "1"
            print(result, end="")
        else:
            result += "0"
            print(result,end="")
    else:
        n = n//2
        print("(", end="")
        div(x,y,n)
        div(x,y+n,n)
        div(x+n,y,n)
        div(x+n,y+n,n)
        print(")", end="")
div(0,0,n)
