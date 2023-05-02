for _ in range(int(input())):
    n,k=list(map(int, input().split()))
    s=input()
    c=0
    a=sorted(set(s))

    for ch in a:
        x=s.count(ch)
        y=s.count(chr(ord(ch)+32))

        s=s.replace(chr(ord(ch)+32), "")

        c+=min(x,y)

        if k>0:
            c+=min(abs(x-y)//2, k)
            k-=min(abs(x-y)//2, k)

    print(c)
