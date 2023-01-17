import sys
while True:
    h = list(map(int, sys.stdin.readline().split()))
    if h[0] == 0:
        break
    else:
        n = h[0]
        h = h[1:]
        stack = []
        area = 0
        for i in range(n):
            while stack and h[i] < h[stack[-1]]:
                height = h[stack[-1]]
                stack.pop() # 끝까지 진행해줘야 하기에 먼저 뺀다. 제일 작은 값 * 해당지점까지 길이
                width = i
                if stack:
                    width = i - stack[-1] - 1
                area = max(height*width, area)
            stack.append(i)
        while stack:
            height = h[stack[-1]]
            stack.pop()
            width = n # 왜냐하면 마지막 지점까지 진행 후 남은 스택으로만 진행하기 때문이다.
            if stack:
                width = n - stack[-1] - 1
            area = max(height*width, area)
        print(area)

