for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    m=a[0]
    s=0

    for i in range(1, n):
        if a[i]^a[i-1] <0:
            s+=m
            m=a[i]
        else:
            m=max(m, a[i])

    print(s+m)