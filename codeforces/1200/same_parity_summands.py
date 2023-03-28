for _ in range(int(input())):
    n, k=list(map(int, input().split()))

    if k>n or (k%2==0 and n%2==1) or (n%2==0 and k%2==1 and k>n//2):
        print('NO')
    else:
        print('YES')
        if n%2==0 and k<=n//2:
            x=2
        else:
            x=1
        
        for i in range(k-1):
            print(x, end=' ')
        
        print(n-(k-1)*x)