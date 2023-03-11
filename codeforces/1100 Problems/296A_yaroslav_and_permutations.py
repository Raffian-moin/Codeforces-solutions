from collections import Counter
n=int(input())
a=list(map(int, input().split()))

counts = Counter(a)
for key, value in counts.items():
    if value > (n+1)//2:
        print('NO')
        break
else:
    print('YES')