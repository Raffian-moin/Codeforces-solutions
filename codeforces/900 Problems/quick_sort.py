import math
for _ in range(int(input())):
    n, k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    x=0
    for i in range(n):
        if a[i]==x+1:
            x+=1

    print(math.ceil((n-x)/k))

    # can also be written as 
    # print((n - c + k - 1) // k)