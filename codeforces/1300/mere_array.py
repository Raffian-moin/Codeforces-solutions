for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=sorted(a)

    for i in range(n):
        if a[i]%b[0]!=0 and a[i]!=b[i]:
            print('NO')
            break
    else:
        print('YES')