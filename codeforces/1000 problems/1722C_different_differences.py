for _ in range(int(input())):
    k, n = list(map(int, input().split()))
    arr = [1]
    x=1


    for i in range(1, k):
        if n-arr[-1]-x>=k-i-1:
            arr.append(arr[-1]+x)
            x+=1
        else:
            arr.append(arr[-1]+1)

    print(*arr)


