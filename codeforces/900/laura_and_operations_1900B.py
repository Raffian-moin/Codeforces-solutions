for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))

    print(1 - (b + c) % 2, 1 - (a + c) % 2, 1 - (a + b) % 2)