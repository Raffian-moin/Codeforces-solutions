for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    s=list(input())
    m=1-int(s[0])
    z=0
    for i in range(1, n):
        if s[i]=='0':
            z+=1
        else:
            if z<k:
                m-=1
            z=0

        if z==k+1:
            z=0
            m+=1

    print(m)