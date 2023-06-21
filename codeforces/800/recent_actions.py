for _ in range(int(input())):
    n,m=list(map(int, input().split()))
    a=list(map(int, input().split()))
    b=[-1]*n
    s=set()
    i=0
    while(i<m and n>=1):
        if a[i] not in s:
            b[n-1]=i+1
            n-=1
        s.add(a[i])
        i+=1

    print(*b)