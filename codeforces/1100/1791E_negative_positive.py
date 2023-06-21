for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    neg = 0
    arr = []

    for i in range(n):
        if a[i] < 0:
            neg+=1
        arr.append(abs(a[i]))

    arr.sort()
    print(sum(arr) if neg%2==0 else sum(arr[1:])-arr[0])

# can also be written as:

# at number 9

# a[i]=-1*(a[i])
# neg+=1

# no need to declare extra array
