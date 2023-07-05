for _ in range(int(input())):
    s=input()
    d={}
    c=1e9+1

    for i in range(len(s)):
        if s[i] not in  d:
            d[s[i]]=[-1, i]
        else:
            d[s[i]].append(i)
    
    for values in d.values():
        m=0
        for i in range(1, len(values)):
            m=max(m, values[i]-values[i-1]-1)

        c=min(c, max(m, len(s)-values[i]-1))
    
    x=0
    while(c>0):
        c=c//2
        x+=1
    # log can be found using
    # bit_length()
    print(x)

    # see answer of 
    # aaaaaaaaaa1