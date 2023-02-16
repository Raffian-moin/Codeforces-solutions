for _ in range(int(input())):  
    n, x, t = list(map(int,input().split()))

    entry = t//x
    if entry < n:
        print(((n-entry)*entry)+((entry-1)*entry//2))
    else:
        print(n*(n-1)//2)

# formula can be different
# q=min(n,t//x)
# print(q*(2*n-q-1)//2)