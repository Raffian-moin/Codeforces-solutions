test_cases = int(input())

while test_cases:


    n, s, r = list(map(int, input().split()))
    arr = [s-r]

    for i in range(n-1):
        arr.append(int(r//(n-1)))

    remainder = r%(n-1)

    index =1 

    while remainder > 0:
        arr[index] = arr[index]+1
        remainder-= 1
        index+=1

    print(*arr)

    test_cases = test_cases-1

    