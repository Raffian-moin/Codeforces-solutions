n=int(input())
a=list(map(int, input().split()))
a.sort()
x=max(a)

for i in range(n-1, 0, -1):
    if a[i]==a[i-1] or x%a[i]!=0:
        print(x, a[i])
        break

# different than editorial
# if constraint is that can't sort the elements than editorial can be used
# otherwise my solution is better