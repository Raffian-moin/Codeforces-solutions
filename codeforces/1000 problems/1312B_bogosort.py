for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort(reverse=True)

    print(*arr)