import math
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    even=a[1]
    odd=a[0]

    if n%2==1:
        a.append(a[-2])

    for i in range(0, len(a)-1, 2):
        odd=math.gcd(odd, a[i])
        even=math.gcd(even, a[i+1])

    even_flag=False
    odd_flag=False

    for i in range(0, len(a)-1, 2):
        if a[i]%even==0:
            odd_flag=True
        if a[i+1]%odd==0:
            even_flag=True
    
    if even_flag and odd_flag:
        print(0)
    elif even_flag:
        print(even)
    else:
        print(odd)
        

    