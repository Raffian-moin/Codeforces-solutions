test_cases = int(input())

while test_cases:


    n, s, r = list(map(int, input().split()))
    arr = [s-r]
    # remaining_dice = n-1
    # print(n-1, r)
    if r%(n-1) == 0:
        for i in range(n-1):
            arr.append(int(r/(n-1)))
    else:
        for i in range(n-2):
            arr.append(int(r//(n-1)))
        arr.append(int(r//(n-1))+r%(n-1))
        
    print(*arr)
    test_cases = test_cases-1
