t = int(input())

while t:
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)


    for i in range(1, len(arr)):
        arr[0] = arr[0]*arr[i]
        arr[i] = 1

    print(sum(arr)*2022)
    
    t = t-1
