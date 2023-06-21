import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x=[]
    participants_on_a_day=[]
    s=set()
    result=[]
    m=int(input())
    for _ in range(m):
        participants_on_a_day.append(int(input()))
        x+=list(map(int, input().split()))

    z=0
    l=m
    flag=False
    for i in range(len(x)-1, -1, -1):
        if z==0:
            l-=1
            z=participants_on_a_day[l]
            flag=False
        if z>0 and x[i] not in s and flag==False:
            result.append(x[i])
            flag=True
        s.add(x[i])
        z-=1

    if len(result)==m:
        print(*result[::-1])
    else:
        print(-1)