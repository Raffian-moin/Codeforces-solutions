for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    first = arr[0]

    for i in range(1, n):
        arr[i] = arr[i]*arr[i-1]


    for i in range(n):
        if arr[(n-1)]/arr[i] == arr[i]:
            print(i+1)
            break
    else:
        print(-1)