for _ in range(int(input())):  
    n, x, t = list(map(int,input().split()))

    entry = t//x
    if entry == n or entry == n-1:
        print(int(((n-1)*n)/2))
    elif entry == 1:
        print(n-1)
    else:
        print(int((n-entry)*entry)+int(((entry-1)*entry)/2))