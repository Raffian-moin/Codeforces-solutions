for _ in range(int(input())):
    n, m, sx, sy, d = list(map(int, input().split()))

    if ( abs(sx-1)<=d and abs(sx-n)<=d ) or ( abs(sy-1)<=d and abs(sy-m)<=d ) or ( abs(sx-n)<=d and abs(sy-m)<=d ) or ( abs(sx-1)<=d and abs(sy-1)<=d ):
        print(-1)
    else:
        print(n+m-2)