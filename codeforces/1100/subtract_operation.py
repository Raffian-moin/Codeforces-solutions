for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    a=set(list(map(int, input().split())))

    for el in a:
        if el-k in a:
            print('YES')
            break
    else:
        print('NO')