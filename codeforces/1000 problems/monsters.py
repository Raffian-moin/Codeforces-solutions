for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    x=0
    c=0
    a.sort()
    
    for el in a:
        if el!=x:
            x+=1
            c+=el-x
    print(c)
