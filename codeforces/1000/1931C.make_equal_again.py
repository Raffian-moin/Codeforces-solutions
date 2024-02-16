for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    left_count = 1
    right_count = 1
    left_flag = True
    right_flag = True

    i = 0

    while (left_flag or right_flag) and i < n - 1:
        if arr[i] != arr[i + 1]:
            left_flag = False
        elif left_flag:
            left_count += 1

        if arr[n - i - 1] != arr[n - i - 2]:
            right_flag = False
        elif right_flag:
            right_count += 1

        i += 1

    if arr[0] != arr[-1]:
        print(n - max(left_count, right_count))
    else:
        print(n - min(n, left_count + right_count))



