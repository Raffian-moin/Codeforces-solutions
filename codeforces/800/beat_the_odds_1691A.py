for _ in range(int(input())):
    n = int(input())

    numbers = list(map(int, input().split()))

    even = 0
    odds = 0

    for i in range(n):
        if numbers[i]%2 == 0:
            even+= 1
        else:
            odds+= 1

    print(min(even, odds))