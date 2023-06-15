for _ in range(int(input())):
    n=int(input())
    s=list(input())
    c=0

    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            s[i]=s[n-i-1]
            c+=1
        elif c>0 and s[i]==s[n-i-1]:
            break
    print('YES' if s==s[::-1] else 'NO')