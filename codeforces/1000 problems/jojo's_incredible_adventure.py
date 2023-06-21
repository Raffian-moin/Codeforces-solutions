for _ in range(int(input())):
    s=input()
    x=[int(x) for x in s]
    one=0
    m=0
    l=0
    r=0
    for i in range(len(x)):
        if x[i]==0:
            one=0
        else:
            one+=1
            m=max(m, one)
        
        if x[0]==1 and m==i+1:
            l=one
        if x[-1]==1 and i==len(x)-1:
            r=one

    if m==len(x):
        print(m*m)
    elif max(m, l+r)>=2:
        print(((max(m, l+r)+1)//2)*((max(m, l+r)+2)//2))
    else:
        print(m)