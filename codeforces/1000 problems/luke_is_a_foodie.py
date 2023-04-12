for _ in range(int(input())):
    n, x=list(map(int, input().split()))
    a=list(map(int, input().split()))
    mi=1000000000
    mx=0
    c=0

    for i in range(n):
        mi=min(mi, a[i])
        mx=max(mx, a[i])
        
        if mx-mi>x*2:
            mi=a[i]
            mx=a[i]
            c+=1

    print(c)
