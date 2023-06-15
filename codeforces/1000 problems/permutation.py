for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int, input().split())))
        
    a.sort()
    b=[]

    if a[0][0] == a[1][0]:
        b=[a[0][0], a[n-1][0]]
    else:
        b=[a[n-1][0], a[0][0]]
        
    for i in range(1, n-1):
        if b[-1]!=a[0][i]:
            b.append(a[0][i])
        else:
            b.append(a[n-1][i])
        
    print(*b)