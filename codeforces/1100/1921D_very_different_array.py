for _ in range(int(input())):
    n, m = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = sorted(list(map(int, input().split())))

    result = 0

    for i in range(n):
        result += max(abs(arr2[n - (i + 1)] - arr1[i]), abs(arr2[-(i + 1)] - arr1[i]))
        
    print(result)