import sys
import math
a, b = map(int, sys.stdin.readline().split())

def cnt_1(x):
    if x <= 0:
        return 0
    else:
        num = int(math.log2(x))
        # num = math.log2(x)
        if 2 ** num == x: # 2의 n승인 경우
            # num = math.log2(x)일 때 2의 n승이 아닌 경우도 int(num) == num이 될 수도 있다. 숫자가 큰 경우
            return int(num) * (x // 2) + 1
        else:
            # step을 낮춰 계산한다.
            y = x - 2**int(num)
            return cnt_1(2**int(num)) + cnt_1(y) + y
print(cnt_1(b) - cnt_1(a-1))
