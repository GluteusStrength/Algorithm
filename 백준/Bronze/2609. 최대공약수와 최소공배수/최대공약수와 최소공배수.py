a,b = input().split()
a = int(a)
b = int(b)
import math
x = math.gcd(a,b)
y = a//x
z = b//x
print(x)
print(x*y*z)