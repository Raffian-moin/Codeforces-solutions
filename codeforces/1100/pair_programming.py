for _ in range(int(input())):
    input()
    k, n, m = list(map(int, input().split()))
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    arr=[]
    x=0
    y=0
    z=0
    flag=0

    while z<(n+m):
        if x<n and a[x]<=k:
            if a[x]==0:
                k+=1
            arr.append(a[x])
            x+=1
        elif y<m and b[y]<=k:
            if b[y]==0:
                k+=1
            arr.append(b[y])
            y+=1
        else:
            flag=1
            break
        z+=1

    
    if flag==1:
        print(-1)
    else:
        print(*arr)

        