for _ in range(int(input())):
    a, b = list(map(int, input().split()))

    count = 0
    flag = 0

    minimum = min(a, b)
    maximum = max(a, b)

    while minimum <= maximum:
        if minimum == maximum:
            flag = 1
            break
        
        minimum *= 2
        count += 1

    if flag == 0:
        print(-1)
    else:
        print(count // 3 + (count % 3) // 2 + (count % 3 % 2))