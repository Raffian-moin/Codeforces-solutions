for _ in range(int(input())):
    n = int(input())
    arr = set(list(map(int, input().split())))

    if len(arr) == 2:
        print(n-(n//2-1))
        # can also be written
        # print(n//2+1)
    else:
        print(n)