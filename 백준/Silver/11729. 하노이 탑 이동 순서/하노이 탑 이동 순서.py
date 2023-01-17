n = int(input())
total = 2**n-1
print(total)
def hanoi(n, x, y, z):
    if n == 1:
        print(x, z)
    else:
        hanoi(n-1, x, z, y)
        print(x,z)
        hanoi(n-1, y, x, z)
hanoi(n, 1, 2, 3)
