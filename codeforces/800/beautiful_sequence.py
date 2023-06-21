for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    for i in range(n-1, -1, -1):
        # don't need to check
        # a[i]<=n
        if a[i]<=n and i+1>=a[i]:
            print('YES')
            break
    else:
        print('NO')