for _ in range(int(input())):
    n=int(input())
    s=input()
    w=s[0]
    x=''

    for i in range(1, n):
        if w=='':
            w=s[i]
        elif s[i]==w:
            x+=w
            w=''

    print(x)