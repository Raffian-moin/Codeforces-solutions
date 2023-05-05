for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    b=[a[(n-1)//2]]
    x=(n-1)//2

    for i in range(1,n):
        if n%2==i%2:
            x=x-i
        else:
            x=x+i
        b.append(a[x])
        
    print(*b)