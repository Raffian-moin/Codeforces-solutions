x,y=input().split()
x=int(x)
s=input()
s+=s
p=len(s)
ans=0
for i in range(len(s)-1,-1,-1):
    print(i)
    if(s[i]=='g'):
        p=i
    if(s[i]==y):
        ans=max(ans,p-i)
print(ans)
