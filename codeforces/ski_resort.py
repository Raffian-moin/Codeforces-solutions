for _ in range(int(input())):
    n,k,q=list(map(int, input().split()))
    a=list(map(int, input().split()))
    x=0
    m=0

    for i in range(n):
        if a[i]<=q:
            x+=1
        else:
            x=0
        m+=max(0, x-k+1)

    print(m)