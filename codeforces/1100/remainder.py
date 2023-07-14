n,x,y=list(map(int, input().split()))
s=input()
c=s[-x:].count('1')

print(c+1 if s[-(y+1)] =='0' else c-1)
