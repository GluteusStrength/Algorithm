n = int(input())
t = [0,1,3]
if n >= 3:
    for i in range(3, n+1):
        ans = (2*t[i-2]) + t[i-1] # 이러한 식이 세워진다. 그 전의 것을 기본으로 하고 거기에 더해서 양끝에 2*2를 채웠을 때를 가정해서 계산하는 것이다.
        t.append(ans)
    print(t[n] % 10007)
else:
    print(t[n])