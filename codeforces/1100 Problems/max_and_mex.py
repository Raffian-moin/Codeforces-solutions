from math import ceil
for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=list(map(int, input().split()))
    a.sort()
    x=0
    for i in range(n):
        if x<a[i]:
            break
        elif x==a[i]:
            x+=1

    if x-1==a[-1]:
        print(len(set(a))+k)
    elif ceil((x+a[-1])/2) not in a and k>0:
        print(len(set(a))+1)
    else:
        print(len(set(a)))