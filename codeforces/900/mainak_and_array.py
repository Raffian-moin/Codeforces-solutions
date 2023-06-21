for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    m=max(a[-1]-a[0], max(a)-a[0], a[-1]-min(a))

    for i in range(n-1):
        m=max(m, a[i]-a[i+1])
    print(m)

    # including last element in the loop
    # ans=max(a[-1]-min(a),max(a)-a[0])
    # for i in range(n):
    #     ans=max(ans,a[i-1]-a[i])
    # print(ans)