for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    t=k//(n-1)

    if k%(n-1)==0:
        print(n*t-1)
    else:
        print(n*t+k%(n-1))

    # elegant answer
    # print(k+(k-1)//(n-1))
