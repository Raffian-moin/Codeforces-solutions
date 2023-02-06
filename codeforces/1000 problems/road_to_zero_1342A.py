for _ in range(int(input())):
    x, y = list(map(int, input().split()))

    a, b = list(map(int, input().split()))

    small = min(x, y)
    big = max(x, y)

    print('0' if x==0 and y==0 else min((big-small)*a + small*b, (small*a+big*a)))