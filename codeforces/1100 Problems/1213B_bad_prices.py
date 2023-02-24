for _ in range(int(input())):
    n= int(input())
    arr = list(map(int, input().split()))
    m=arr[n-1]
    c=0
    for i in range(n-2, -1, -1):
        if arr[i] > m:
            c+=1
        else:
            m=arr[i]

    print(c)
