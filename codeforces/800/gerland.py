from collections import Counter
for _ in range(int(input())):
    s=input()
    l = Counter(s)
    m=0
    for v in l.values():
        m=max(m, v)
    
    if m==4:
        print(-1)
    elif m==3:
        print(6)
    else:
        print(4)


# can also written as for max count of counter
# max(l.values())