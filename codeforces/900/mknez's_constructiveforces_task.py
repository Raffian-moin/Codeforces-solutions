for _ in range(int(input())):
    n=int(input())
    if n==3:
        print('NO')
    else:
        print('YES')
        if n%2==0:
            print(*[1,-1]*(n//2))
        else:
            k = n//2
            print(*[1-k,k]*k,1-k)