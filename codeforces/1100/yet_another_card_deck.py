import sys
input = sys.stdin.readline
n,q=list(map(int, input().split()))
a=list(map(int, input().split()))
b=list(map(int, input().split()))
pos={}

for i in range(n):
    if a[i] not in pos:
        pos[a[i]]=i+1

for el in b:
    po=pos[el]
    print(po, end=" ")
    for x, y in pos.items():
        if y<po:
            pos[x]+=1

    pos[el]=1
    