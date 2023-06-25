for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    x=a[0]
    flag=0
    for i in range(n):
        if a[i]>=x and a[i]>=a[0] and flag==0:
            x=a[i]
            print(1, end="")
        elif flag==0 and a[i]<=a[0]:
            print(1, end="")
            flag=1
            x=a[i]
        elif a[i]>=x and a[i]<=a[0]:
            print(1, end="")
            x=a[i]
        else:
            print(0, end="")
        
    print()

