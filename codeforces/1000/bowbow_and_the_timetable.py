s=input()
ans=(len(s)+1)//2
if len(s)&1 and '1' not in s[1:]:
    ans-=1
print(ans)