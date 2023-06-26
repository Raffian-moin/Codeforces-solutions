for _ in range(int(input())):
    n=int(input())
    s='-'+input()+'-'
    m=0
    x=1
    for i in range(1, n+2):
        if s[i]==s[i-1]:
            x+=1
        else:
            m=max(m, x)
            x=1

    print(m+1)