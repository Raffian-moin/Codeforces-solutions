import sys
for _ in range(int(input())):
    n=int(input())
    a=sorted(list(map(int, input().split())))
    even=sys.maxsize
    odd=sys.maxsize
    for el in a:
        if el%2==1:
            odd=min(odd, el)
        else:
            even=min(even, el)

    if even!=sys.maxsize and odd!=sys.maxsize and even<odd:
        print('NO')
    else:
        print('YES')