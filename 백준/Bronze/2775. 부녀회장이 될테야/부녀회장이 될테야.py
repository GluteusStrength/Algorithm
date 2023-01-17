t = int(input())
floor = []
for i in range(t):
    floor.append([int(input()) for _ in range(2)])
p = [[i for i in range(15)]]
for i in range(14):
    ch = []
    for j in range(15):
        ch.append(sum(p[i][:j+1]))
    p.append(ch)
for i in floor:
    print(p[i[0]][i[1]])