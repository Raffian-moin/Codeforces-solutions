n=int(input())
a=['0']+list(input())
b=['0']+list(input())
ans=0
for i in range(n+1):
    if a[i]!=b[i]:
        ans+=1

        if a[i]+a[i-1]==b[i-1]+b[i]:
            ans-=1
            a[i]='0'
            b[i]='0'

print(ans)