import math
n = int(input())
def isprime(x):
    num = x
    if num % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
def make(a):
    s = a
    if len(str(s)) == n:
        print(s)
    else:
        odd_list = [1, 3, 5, 7, 9]
        for i in odd_list:
            cnt = s*10 + i
            if isprime(cnt) == True:
                make(cnt)

prime_l = [2, 3, 5, 7]
for i in prime_l:
    make(i)
