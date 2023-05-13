import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,h=list(map(int, input().split()))
    a=list(map(int, input().split()))
    mi=(h+n-1)//n
    b=[]
    for i in range(1, n):
        b.append(a[i]-a[i-1])

    b.sort()

    for i in range(n-1):
        if mi<=b[i]:
            break
        h-=b[i]
        mi=max(mi, (h+n-i-2)//(n-i-1))

    print(mi)