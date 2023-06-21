n, k=list(map(int, input().split()))
a=[1]+list(map(int, input().split()))
a.sort()
a.append(a[-1]+1)

if a[k]==a[k+1]:
    print(-1)
else:
    print(a[k])