for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    a_sum=sum(a)
    b_sum=sum(b)
    # we don't need sum of b
    x=0
    y=0
    z=a_sum+b_sum
    # can be written as
    # z=sys.maxsize
    for i in range(n):
        x+=a[i]
        z=min(z, max(a_sum-x, y))
        y+=b[i]

    print(z)
