for _ in range(int(input())):
    a, b, x, y, n = list(map(int, input().split()))
    k=max(n-(a-x),0)
    r=max(n-(b-y),0)
    print(min((a-(n-k))*max(b-k, y), (b-(n-r))*max(a-r, x)))