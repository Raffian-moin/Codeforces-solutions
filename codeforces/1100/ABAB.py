for _ in range(int(input())):
    s=input()
    b=0
    c=0

    for i in range(len(s)-1, -1, -1):
        if s[i]=='B':
            b+=1
        if b>0 and s[i]=='A':
            b-=1
            c+=1
    if (s.count('B')-c)%2==0:
        print(s.count('A')-c)
    else:
        print(s.count('A')-c+1)