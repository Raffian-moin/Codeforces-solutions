for _ in range(int(input())):
    n = int(input())

    s = input()

    first = 0
    last = n-1

    maximum = 0

    while last>=first:
        if s[first] == '1' or s[last] == '1':
            maximum = max(maximum, n-first)
        first+=1
        last-=1

    print(n if maximum == 0 else maximum*2)