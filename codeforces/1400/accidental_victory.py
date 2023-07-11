from itertools import accumulate
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=[]
    ans=1

    for i in range(n):
        b+=[[a[i], i+1]]

    a.sort()
    c=list(accumulate(a))
    b.sort(key=lambda x:x[0])
    l=[b[-1][1]]

    for i in range(n-2, -1, -1):
        if c[i]<b[i+1][0]:
            break
        ans+=1
        l.append(b[i][1])

    print(ans)
    print(*(sorted(l)))