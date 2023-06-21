for _ in range(int(input())):
    n, m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x=0
    while x<m:
        a.sort()
        a[0]=b[x]
        x+=1

    print(sum(a))