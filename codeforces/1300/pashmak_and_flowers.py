n=int(input())
a=list(map(int, input().split()))
a.sort()
if a[-1]==a[0]:
    print(a[-1]-a[0], n*(n-1)//2)
else:
    print(a[-1]-a[0], a.count(a[0])*a.count(a[-1]))