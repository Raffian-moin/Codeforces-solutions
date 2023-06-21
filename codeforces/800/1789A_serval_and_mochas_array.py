import math
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    for i in range(n):
        for j in range(i+1, n):
            if math.gcd(a[i], a[j]) <=2:
                flag=1
                break
        if flag==1:
            break

    print('Yes' if flag==1 else 'No')