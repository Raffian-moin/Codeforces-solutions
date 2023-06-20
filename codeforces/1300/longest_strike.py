for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    a.sort()
    m=0
    x=a[0]
    y=a[0]
    values=[x, y]
    c=0
    flag=False

    for i in range(n):
        if a[i]==y:
            c+=1
        elif c<k or a[i]!=y+1:
            x=a[i]
            y=a[i]
            c=1
        else:
            y=a[i]
            c=1

        if c>=k and y-x>=m:
            flag=True
            m=y-x
            values=[x, y]

    if flag:
        print(*values)
    else:
        print(-1)
        

