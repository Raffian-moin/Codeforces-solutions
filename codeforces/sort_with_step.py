for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    c=0
    for i in range(n):
        if (i+1)%k != a[i]%k:
            c+=1

    if c==0:
        print(0)
    elif c==2:
        print(1)
    else:
        print(-1)