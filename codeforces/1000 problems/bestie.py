import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    if math.gcd(*a)==1:
        print(0)
    elif math.gcd(*a, math.gcd(n, a[-1]))==1:
        print(1)
    elif math.gcd(*a, math.gcd(n-1, a[-2]))==1:
        print(2)
    else:
        print(3)

    # can also be written as 
    #  if math.gcd(*a)==1:
    #     print(0)
    # elif math.gcd(*a, n)==1:
    #     print(1)
    # elif math.gcd(*a, n-1)==1:
    #     print(2)
    # else:
    #     print(3)