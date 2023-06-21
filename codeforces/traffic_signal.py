for _ in range(int(input())):
    n,c=input().split()
    s=input()
    s+=s
    n=int(n)
    m=0
    start=-1

    for i in range(n*2):
        if s[i]==c and start==-1:
            start=i
        if start>=0 and s[i]=='g':
            m=max(m, i-start)
            start=-1
            if i>=n:
                break

    print(m)