for _ in range(int(input())):
    n=int(input())
    s=input()
    w=s[:2]
    c=n-1
    for i in range(2, n):
        if s[i-1:i+1][::-1]==w:
            c-=1
        w=s[i-1:i+1]

    print(c)

    # can also be written as 
    # ans = n-1
    # for i in range(n-2):
    #     ans-=(st[i]==st[i+2])
    # print(ans)
