for _ in range(int(input())):
    a, b = list(map(int, input().split()))

    print((min(a, b)+min(min(a, b)*2, max(a, b)))//3)
