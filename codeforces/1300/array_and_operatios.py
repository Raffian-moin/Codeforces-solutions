for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    a.sort()
    s=0
    for i in range(n-1, n-k-1, -1):
        if a[i-k]/a[i]==1:
            s+=1
        # can also be written:
        # s+=a[i-k]//a[i] 
    print(s+sum(a[:n-k*2]))
