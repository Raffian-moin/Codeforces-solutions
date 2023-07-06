for _ in range(int(input())):
    s=input()
    f_one=0
    f_un=0
    s_one=0
    s_un=0

    for i in range(1, 11):
        if i&1 and s[i-1]=='1':
            f_one+=1
        elif i&1 and s[i-1]=='?':
            f_un+=1
        elif s[i-1]=='1':
            s_one+=1
        elif s[i-1]=='?':
            s_un+=1
        
        if f_one+f_un>s_one+(10-i+1)//2 or s_one+s_un>f_one+(10-i)//2:
            print(i)
            break
    else:
        print(10)

    
