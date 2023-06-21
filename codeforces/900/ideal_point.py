for _ in range(int(input())):
    n, k=list(map(int, input().split()))
    l=[]
    r=[]

    for _ in range(n):
        a, b=list(map(int, input().split()))
        l.append(a)
        r.append(b)

    if k in l and k in r:
        print('YES')
    else:
        print('NO')