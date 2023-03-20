for _ in range(int(input())):
    a, b, c, d=list(map(int, input().split()))

    if a+d-b < c or b>d:
        print(-1)
    else:
        print(d-b+ (a+d-b)-c)