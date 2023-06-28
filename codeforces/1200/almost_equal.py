n=int(input())
if not n&1:
    print('NO')
else:
    print('YES')
    a=[]
    b=[]
    for i in range(1, n+1):
        if i&1 and i<=n:
            a.append(i*2-1)
            b.append(i*2)
        elif i<=n:
            a.append(i*2)
            b.append(i*2-1)
    print(*(a+b))