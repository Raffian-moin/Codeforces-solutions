for _ in range(int(input())):
    n=int(input())
    a=sorted(list(map(int, input().split())))
    x=[]

    if n&1:
        print('NO')
    else:
        z=n//2
        for i in range(n//2):
            if len(x)>0 and (a[i]==x[-1] or a[i]==a[i+z]):
                print('NO')
                break
            x+=[a[i], a[i+z]]  
        else:
            print('YES')
            print(*x)