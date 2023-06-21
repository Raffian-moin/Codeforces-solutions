for _ in range(int(input())):
    a, b, n, s = list(map(int,input().split()))

    print('YES' if (s-min(a, s//n)*n) <= b else 'NO')
