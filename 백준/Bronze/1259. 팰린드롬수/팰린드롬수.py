while True:
    num = input()
    if num == '0':
        break
    else:
        if len(num) % 2 == 0:
            flag = len(num) // 2
            front = num[:flag]
            back = num[flag:]
            if front == back[::-1]:
                print("yes")
            else:
                print("no")
        else:
            flag = len(num) // 2
            front = num[:flag]
            back = num[flag+1:]
            if front == back[::-1]:
                print("yes")
            else:
                print("no")