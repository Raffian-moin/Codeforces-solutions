for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))

    one=a.index(1)
    two=a.index(2)
    h=a.index(max(a))
    if abs(one-two)==1 and h<min(one, two):
        z=min(one, two)+1
    elif abs(one-two)==1 and h>min(one, two):
        z=max(one, two)+1
    else:
        z=min(one, two)+2
    print(h+1, z)