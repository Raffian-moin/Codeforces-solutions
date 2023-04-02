for _ in range(int(input())):
    n, x, y=list(map(int, input().split()))

    if min(x, y)>0 or max(x,y)<1 or (n-1)%max(x, y)!=0:
        print(-1)
    else:

        # can be also written as 
        # i = 0
        # w = 0
        # while i < n-1:
        #     if i%y == 0:
        #         w = i+2
        #     print(w, end=" ")
        #     i += 1
        a=[1]*(n-1)
        m=max(x, y)
        z=2+m
        p=1
        for i in range(m, n-1):
            a[i]=z
            p+=1
            if p>m:
                z+=m
                p=1
        print(*a)

