for _ in range(int(input())):
    n=int(input())
    a=input()
    d=[]
    c=0
    for i in range(n):
        if a[i]=='L':
            c+=i
            d.append((n-i-1)-i)

        else:
            c+=n-i-1
            d.append(i-(n-i-1))

    d.sort(reverse=True)
    ans=[]
    for i in range(0, n):
        c+=max(d[i], 0)
        ans.append(c)
    print(*ans)