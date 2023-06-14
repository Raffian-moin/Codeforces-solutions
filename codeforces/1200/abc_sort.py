for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    if n%2==1:
        a=[0]+a

    b=sorted(a)
    
    for i in range(0, n, 2):
        if a[i] not in [b[i], b[i+1]] or a[i+1] not in [b[i], b[i+1]]:
            print('NO')
            break
    else:
        print('YES')