for _ in range(int(input())):
    n = int(input())
    blocks = list(map(int, input().split()))

    first = blocks[0]
    blocks.sort()

    sorted_arr = blocks[blocks.index(first):]

    for i in range(1, len(sorted_arr)):
        if sorted_arr[i]-first >=1:
            first+= (sorted_arr[i]-first+1)//2

    print(first)