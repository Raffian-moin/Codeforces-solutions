for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=[0]*3
    x=n//3
    ans=0

    for el in a:
        b[el%3]+=1

    for i in range(3):
        ans+=max(b[i-1]-x, x-b[i], 0)
        b[i]+=max(b[i-1]-x, x-b[i], 0)

    print(ans)