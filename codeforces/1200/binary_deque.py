import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,s=list(map(int, input().split()))
    a=list(map(int, input().split()))
    m=n
    b=[]
    c=0

    for i in range(n):
        if a[i]==1:
            b.append(i)
    
    for i in range(len(b)):
        l=0
        r=0
        c+=1
        if c==s:
            if i+1-s>0:
                l=b[i-s]+1
            if i!=len(b)-1:
                r=n-b[i+1]
            m=min(m, l+r)
            c-=1
            
    if s>sum(a):
        m=-1
    print(m)