for _ in range(int(input())):
    n, x, y = list(map(int, input().split()))

    mi = min(x, y)
    ma = max(x, y)

    common_divisor = 0
    com = 0


    for num in range(ma, n + 1, ma):
        if num % mi == 0:
            common_divisor = num
            break

    if common_divisor:
        com = n // common_divisor

    p = n // x - com
    q = n // y - com

    print((((n * (n + 1)) // 2) - (((n - p) * (n - p + 1)) // 2)) - ((q * (q + 1)) // 2))



# Efficient solution:
# The idea is to find the L.C.M of the two x and y

# import math
# for _ in range(int(input())):
#     n, x, y = list(map(int, input().split()))

#     com = n // math.lcm(x, y)

#     p = n // x - com
#     q = n // y - com

#     print((((n * (n + 1)) // 2) - (((n - p) * (n - p + 1)) // 2)) - ((q * (q + 1)) // 2))

