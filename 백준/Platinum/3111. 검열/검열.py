import sys
a = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()
a_back = a[::-1]
t_back = t[::-1]
front = []
back = []
ind_f = 0
ind_b = len(t) - 1
while ind_f <= ind_b: # 없다면 그대로 쭉 통과될 코드이다.
    while ind_f <= ind_b:
        front.append(t[ind_f])
        ind_f += 1
        if len(front) >= len(a) and "".join(front[-len(a):]) == a:
            del front[-len(a):]
            break
    while ind_f <= ind_b:
        back.append(t[ind_b])
        ind_b -= 1
        if len(back) >= len(a) and "".join(back[-len(a):]) == a_back:
            del back[-len(a):]
            break
ans = front + list(reversed(back))
x = 0
while x >= 0:
    x = "".join(ans).find(a) # 문자열에서 a라는 뭉탱이의 첫번째 index를 반환
    if x != -1: # a가 문자열에 존재하지 않는 경우
        del ans[x:x+len(a)]
print("".join(ans))