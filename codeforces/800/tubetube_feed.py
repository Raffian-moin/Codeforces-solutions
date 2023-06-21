for _ in range(int(input())):
    n, t=list(map(int, input().split()))
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    m=0
    index=-1
    for i in range(n):
        if t>=a[i]:
            if b[i]>=m:
                index=i+1
                m=b[i]
        t-=1
    print(index)