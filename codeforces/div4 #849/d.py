for _ in range(int(input())):
    n=int(input())
    st = input()

    mid = n//2
    left = len(set(st[:mid]))
    right = len(set(st[mid:]))


    for i in range(mid):
        left1 = len(set(st[:mid+1]))
        right1 = len(set(st[mid+1:]))

        left2 = len(set(st[:mid-1]))
        right2 = len(set(st[mid-1:]))

        
        print(left1, right1)
        print(left2, right2)

        if (left1 > left and right1 == right):
            print('ok')
            left = left1
            right = right1
            mid = mid+1
        elif (left2 == left and right2 > right):
            print('ok2')
            left = left2
            right = right2
            mid = mid-1
        else:
            break
    
    print(left+right)
