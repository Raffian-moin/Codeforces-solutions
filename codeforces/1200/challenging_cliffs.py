for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    l=(n-2)//2
    r=n//2
    m=1000000000
    for i in range(1, n):
        if a[i]-a[i-1]<m:
            m=a[i]-a[i-1]
            l=i-1
            r=i

    print(*([a[l]]+a[r+1:]+a[:l]+[a[r]]))