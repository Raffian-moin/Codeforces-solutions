for _ in range(int(input())):
    a, b=list(map(int, input().split()))

    if a==1 or b==1:
        print(1)
        print(a, b)
    else:
        print(2)
        print(1, b-1)
        print(a, b)

# answer will be only 
# print(2)
# print(1, b-1)
# print(a, b)
# because we can also jump grid lines, not necessarily konakuni