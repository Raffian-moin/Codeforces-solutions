for _ in range(int(input())):
    n, k=list(map(int, input().split()))

    if n%2==k%2 or n%2==0:
        print('YES')
    else:
        print('NO')