from collections import Counter
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    c = Counter(s)
    if any(x == 1 for x in c.values()):
        print(-1)
        continue
        
    print(*[i if i!=0 and s[i]==s[i-1] else i+c[s[i]] for i in range(n)])
