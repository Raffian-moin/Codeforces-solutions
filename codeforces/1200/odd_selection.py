for _ in range(int(input())):
    n,x=list(map(int, input().split()))
    a=list(map(int, input().split()))
    c=0
    for y in a:
        if y%2==1:
            c+=1
    
    if c==0:
        print('No')
    elif n==x and c%2==0:
        print('No')
    elif n==c and x%2==0:
        print('No')
    else:
        print('Yes')