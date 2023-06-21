for _ in range(int(input())):
    n=int(input())
    a = list(map(int, input().split()))
    a.sort()

    p=0
    e=0
    o=0
    i=0

    for element in a:
        if element%2==0:
            e+=1
        else:
            o+=1
    while i<n-1:
        if a[i+1]-a[i]==1:
            p+=1
            i+=2
        else:
            i+=1

    if e%2==0 or (e%2==1 and p>0):
        print('YES')
    else:
        print('NO')