from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    s=[input()for _ in range(n)]
    count=defaultdict(int)
    first, last=defaultdict(int), defaultdict(int)
    m=0
    for el in s:
        m+=first[el[0]]+last[el[1]]-2*count[el]
        first[el[0]]+=1
        last[el[1]]+=1
        count[el]+=1

    print(m)


