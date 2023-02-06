t = int(input())

while t:
    n, m = input().split()

    arr = list(map(int,input().split()))

    b = list(map(int,input().split()))

    arr.sort()
    # b.sort()
    index = 0
    for i in range(len(b)):
        arr[index] = b[i]
        index = index+1
        if index == len(arr):
            index = 0

    print(sum(arr))
    t = t-1