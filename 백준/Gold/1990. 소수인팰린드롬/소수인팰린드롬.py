a,b = map(int, input().split())
import math
def isprime(x, k):
    eratos = [1] * (x)
    s = int(math.sqrt(x))
    for i in range(2, s + 1):
        if eratos[i] == 1:
            for j in range(i + i, x, i):
                eratos[j] = 0
    z = k
    return [str(y) for y in range(z, x) if eratos[y] == 1 and (
                (str(y)[0] == "1" and str(y)[-1] == "1") or (str(y)[0] == "3" and str(y)[-1] == "3") or (
                    str(y)[0] == "7" and str(y)[-1] == "7") or (str(y)[0] == "9" and str(y)[-1] == "9"))]
# 10만 단위의 경우는 palindrome이 존재하지 않는다.
if b >= 100000 and b < 1003001:
    b = 100000
    if a >= b:
        print(-1)
    else:
        l = isprime(b,a)
        ans = []
        for i in l:
            if len(i) == 1 or len(i) == 2 or len(i) == 3:
                ans.append(i)
            elif len(i) == 4:
                if i[1] == i[2]:
                    ans.append(i)
            else:
                if i[1] == i[3]:
                    ans.append(i)
        if ans == []:
            print(-1)
        else:
            if a == 5:
                print(5)
                for i in ans:
                    print(int(i))
                print(-1)
            else:
                for i in ans:
                    print(i)
                print(-1)
elif b < 100000:
    l = isprime(b,a)
    ans = []
    for i in l:
        if len(i) == 1 or len(i) == 2 or len(i) == 3:
            ans.append(i)
        elif len(i) == 4:
            if i[1] == i[2]:
                ans.append(i)
        else:
            if i[1] == i[3]:
                ans.append(i)
    if ans == []:
        if a == 5:
            print(5)
            print(-1)
        else:
            print(-1)
    else:
        if a == 5:
            print(5)
            for i in ans:
                print(int(i))
            print(-1)
        else:
            for i in ans:
                print(int(i))
            print(-1)
else:
    eratos = []
    # palindrome 숫자를 먼저 구해본다.
    def check_isp(n):
        if n % 2 == 0:
            return False
        else:
            for i in range(3, int(math.sqrt(n))+1, 2):
                if n % i == 0:
                    return False
        return True
    if a >= 1003001:
        if a < b:
            for i in range(a, b+1):
                num = str(i)
                if len(num) == 7:
                    if (num[0] == "1" and num[-1] == "1") or (num[0] == "3" and num[-1] == "3") or (num[0] == "7" and num[-1] == "7") or (num[0] == "9" and num[-1] == "9"):
                        if num[1] == num[5]:
                            if num[2] == num[4]:
                                if check_isp(int(num)) == True:
                                    eratos.append(int(num))
                if len(num) == 8:
                    if (num[0] == "1" and num[-1] == "1") or (num[0] == "3" and num[-1] == "3") or (num[0] == "7" and num[-1] == "7") or (num[0] == "9" and num[-1] == "9"):
                        if num[1] == num[6]:
                            if num[2] == num[5]:
                                if num[3] == num[4]:
                                    if check_isp(int(num)) == True:
                                        eratos.append(int(num))
            if eratos == []:
                print(-1)
            else:
                for i in eratos:
                    print(i)
                print(-1)
        else:
            if a == b:
                if check_isp(a) != False:
                    print(-1)
                else:
                    print(a)
                    print(-1)
            else:
                print(-1)
    else:
        for i in range(a, b + 1):
            num = str(i)
            if len(num) == 7:
                if (num[0] == "1" and num[-1] == "1") or (num[0] == "3" and num[-1] == "3") or (
                        num[0] == "7" and num[-1] == "7") or (num[0] == "9" and num[-1] == "9"):
                    if num[1] == num[5]:
                        if num[2] == num[4]:
                            if check_isp(int(num)) == True:
                                eratos.append(int(num))
            if len(num) == 8:
                if (num[0] == "1" and num[-1] == "1") or (num[0] == "3" and num[-1] == "3") or (
                        num[0] == "7" and num[-1] == "7") or (num[0] == "9" and num[-1] == "9"):
                    if num[1] == num[6]:
                        if num[2] == num[5]:
                            if num[3] == num[4]:
                                if check_isp(int(num)) == True:
                                    eratos.append(int(num))
        ans = []
        l = isprime(100000,a)
        for i in l:
            if len(i) == 1 or len(i) == 2 or len(i) == 3:
                ans.append(i)
            elif len(i) == 4:
                if i[1] == i[2]:
                    ans.append(i)
            else:
                if i[1] == i[3]:
                    ans.append(i)
        final = ans + eratos
        if a == 5:
            print(a)
        for x in final:
            print(x)
        print(-1)