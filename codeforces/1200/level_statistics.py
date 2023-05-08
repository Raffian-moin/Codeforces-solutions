for _ in range(int(input())):
    n=int(input())
    x,z=-1, -1
    ans='YES'
    for i in range(n):
        p,c=list(map(int, input().split()))
        if ans=='YES':
            if c>p:
                ans='NO'
            if c-z>p-x:
                ans='NO'
            if p<x or c<z:
                ans='NO'
            x,z=p,c

    print(ans)

    # can also be written as 
    # for i in range(n):
    #     p,c=list(map(int, input().split()))
    #         if c>p or c-z>p-x or p<x or c<z:
    #             ans='NO'
    #         x,z=p,c

    # print(ans)