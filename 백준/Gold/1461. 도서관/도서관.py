import sys
import math # 내일 해결한다 시발
n, m = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))
books.sort()
move = 0
left = []
right = []
for i in books:
    if i <= 0:
        left.append(i)
    else:
        right.append(i)
if not left and right: # right에만 있다는 소리
    dist = []
    while len(right) >= m:
        for i in range(m):
            if i == 0:
                dist.append(right.pop())
            else:
                if right:
                    right.pop()
    if not dist and right:
        move += right[-1]
    elif dist and not right:
        for i in range(len(dist)):
            if i == 0:
                move += dist[i]
            else:
                move += dist[i]*2
    else:
        move += right[-1] * 2
        for i in range(len(dist)):
            if i == 0:
                move += dist[i]
            else:
                move += dist[i]*2
    print(move)
elif not right and left: #left에만 있다는 소리
    dist = []
    while len(left) >= m:
        for i in range(m):
            if i == 0:
                dist.append(left.pop(0))
            else:
                if left:
                    left.pop(0)
    if not dist and left: # 들 수 있는 책의 개수가 더 많은 case
        move += -left[0]
    elif dist and not left:
        for i in range(len(dist)):
            if i == 0:
                move += -dist[i]
            else:
                move += -dist[i] * 2
    else:
        move += -left[0] * 2
        for i in range(len(dist)):
            if i == 0:
                move += -dist[i]
            else:
                move += -dist[i] * 2
    print(move)
else:
    x = max(-left[0], right[-1])
    if -left[0] >= right[-1]:
        dist_l = []
        move += int(x)
        for _ in range(m):
            if left:
                left.pop(0)
            else:
                break
        if left:
            while len(left) >= m:
                for i in range(m):
                    if i == 0:
                        dist_l.append(left.pop(0))
                    else:
                        left.pop(0)
            if not dist_l and left:
                move += (-left[0]) * 2
            elif dist_l and not left:
                move += (-sum(dist_l)) * 2
            else:
                move += (-left[0]) * 2
                move += (-sum(dist_l)) * 2
        dist_r = []
        while len(right) >= m:
            for i in range(m):
                if i == 0:
                    dist_r.append(right.pop())
                else:
                    right.pop()
        if not dist_r and right:
            move += right[-1] * 2
        elif dist_r and not right:
            move += sum(dist_r) * 2
        else:
            move += right[-1] * 2
            move += sum(dist_r) * 2
        print(move)
    else:
        dist_r = []
        for i in range(m):
            if right:
                if i == 0:
                    move += right.pop()
                else:
                    right.pop()
            else:
                break
        if right:
            while len(right) >= m:
                for i in range(m):
                    if i == 0:
                        dist_r.append(right.pop())
                    else:
                        right.pop()
            if not dist_r and right:
                move += right[-1] * 2
            elif dist_r and not right:
                move += sum(dist_r) * 2
            else:
                move += right[-1] * 2
                move += sum(dist_r) * 2
        dist_l = []
        while len(left) >= m:
            for i in range(m):
                if i == 0:
                    dist_l.append(left.pop(0))
                else:
                    left.pop(0)
        if not dist_l and left:
            move += (-left[0]) * 2
        elif dist_l and not left:
            move += (-sum(dist_l)) * 2
        else:
            move += (-left[0]) * 2
            move += (-sum(dist_l)) * 2
        print(move)




