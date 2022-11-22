
test_cases = int(input())

while test_cases:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    diff_min = 0

    for index in range(n-1,0,-1):
        if l[index] - l[index-1] != 0:
            diff = l[index] - l[index-1]
            if diff != diff_min and diff_min%diff ==0:
                diff_min = diff

    if diff_min > 1:
        print(diff_min)
    else:
        print(-1)

    test_cases = test_cases-1