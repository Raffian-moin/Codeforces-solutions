for _ in range(int(input())):
    n=int(input())
    x=n
    i=0
    a=[]

    if n%2==0:
        print(-1)
    else:
        while(i<n and x>3):
            if (x//2)%2==1:
                a.append(2)
                x=x//2
            else:
                a.append(1)
                x=(x//2)+1
            i+=1

        c=[2]+a[::-1]
        print(len(c))
        print(*c)