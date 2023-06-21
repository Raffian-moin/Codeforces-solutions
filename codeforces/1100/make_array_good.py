import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    print(n)
    for i in range(n):
        print(i+1, 2**(math.floor(math.log(a[i], 2)+1))-a[i])