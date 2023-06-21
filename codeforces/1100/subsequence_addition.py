for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    s=a[0]
    if a[0]!=1:
        print('NO')
    else:
        for i in range(1, n):
            if a[i] > s:
                print('NO')
                break
            s+=a[i]
        else:
            print('YES')