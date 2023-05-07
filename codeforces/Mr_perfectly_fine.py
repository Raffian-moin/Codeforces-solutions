import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    f=10**10
    s=10**10
    b=10**10
    m=10**10
    for _ in range(n):
        mi, sk=list(map(str, input().split()))
        mi=int(mi)
        if sk=='11':
            m=min(m, mi)
        elif sk=='01':
            f=min(f, mi)
        elif sk=='10':
            s=min(s, mi)
            
        m=min(m, s+f)

    print(-1 if m==10**10 else m)

    # can also be written as 
    # for _ in range(n):
    #     mi, sk=list(map(str, input().split()))
    #     mi=int(mi)
    #     if sk=='11':
    #         m=min(m, mi)
    #     elif sk=='01':
    #         f=min(f, mi)
    #     elif sk=='10':
    #         s=min(s, mi)
            
    # out of the loop
    # m=min(m, s+f)
    # print(-1 if m==10**10 else m)