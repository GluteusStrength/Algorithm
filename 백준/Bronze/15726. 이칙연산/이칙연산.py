import sys
a,b,c = map(int, sys.stdin.readline().split())
case_1 = (a*b)/c
case_2 = (a/b)*c
print(int(max(case_1, case_2)))