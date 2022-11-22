test_cases = int(input())

while test_cases:

    n, k = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    arr.sort()

    cat_position = 0
    rescued = 0

    for index in range(k-1,-1,-1):
        if arr[index] == n:
            rescued = rescued + 1
        elif arr[index] <= n:
            if cat_position < arr[index]:
                rescued = rescued + 1
                cat_position = cat_position + n - arr[index]

    print(rescued)

    test_cases = test_cases - 1
