from collections import Counter
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    c = Counter(a)
    x=-1
    m=1e9
    for value in c:
        if value!=x+1 or c[value] > m:
            print('NO')
            break
        x=value
        m=c[value]
    else:
        print('YES')