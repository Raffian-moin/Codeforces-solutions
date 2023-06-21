import math
for i in range(int(input())):
    n=int(input())
    if n%2==0:
        print(n//2, n//2)
    else:
        for i in range(3, math.isqrt (n)+1, 2):
            # print(math.isqrt (n)+1)
            if n%i==0:
                print(n//i, n-(n//i))
                break
        else:
            print(1, n-1)