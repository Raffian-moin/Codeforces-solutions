import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=[]
    ans=0
    for _ in range(n):
        a+=[list(map(int, input().split()))]

    for el in a:
        if el[0]-el[1]>0:
            ans+=1
    print(ans)