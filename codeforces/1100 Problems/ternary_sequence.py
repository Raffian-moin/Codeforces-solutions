for i in range(int(input())):
    a, b, c=list(map(int, input().split()))
    d, e, f=list(map(int, input().split()))

    print(min(c, e)*2+ min(0, (c-min(c, e)-(f-min(a, f)))*2))