for _ in range(int(input())):
    n = int(input())

    last = (n + 3) // 4

    print((n - last) * '9' + last * '8')