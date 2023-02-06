n, m, sx, sy, d = list(map(int, input().split()))

if (sx+d == n or sy+d==m) or (sx-d == 1 and sx+d == n) or(sx-d == 1 and sx+d == n):
    print(-1)
else:
    print(n+m-2)