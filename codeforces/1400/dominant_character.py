import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    s=input()
    x=s.split('a')
    m=1e9

    if len(x)>1:
        for i in range(1, len(x)-1):
            w=x[i]
            l=len(w)
            if l==len(set(w)):
                m=min(m, l+2)
            elif l==2 and len(x[i-1])==2 and w!=x[i-1] and i>1:
                m=min(m, 7)
    
    print(-1 if m==1e9 else m)