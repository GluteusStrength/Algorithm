import sys
n = int(sys.stdin.readline())
mem = []
for _ in range(n):
    x, y = map(str, sys.stdin.readline().split())
    mem.append([int(x), y])
mem.sort(key = lambda x : x[0])
for i in range(n):
    print(mem[i][0], mem[i][1])