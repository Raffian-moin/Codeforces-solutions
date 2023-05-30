import math
for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=['a']*n
    x=int(math.ceil((math.sqrt((8*k)+1)-1)/2))+1
    y=int((((x-1)*x)//2)-k)
    a[-x]='b'
    a[-x+y+1]='b'
    print("".join(a))