for _ in range(int(input())):
    input()
    a=[]
    for _ in range(8):
        a+=[list(input())]


    for i in range(8):
        if len(set(a[i]))==1 and 'R' in set(a[i]):
            print('R')
            break
        x=set()
        for j in range(8):
            x.add(a[j][i])
        if len(x)==1 and 'B' in x:
            print('B')
            break