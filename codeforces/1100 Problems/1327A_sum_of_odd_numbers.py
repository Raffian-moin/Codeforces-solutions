for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    rn = n%2
    rk = k%2

    if rn!=rk or n/k < k:
        print('NO')
    else:
        print('YES')