for _ in range(int(input())):  
    n = int(input())

    arr = list(map(int,input().split()))

    if n%2 == 1:
        print('Mike')
    else:
        minimum = min(arr)
        index = arr.index(minimum)
        print('Joe' if index%2 == 0 else 'Mike')