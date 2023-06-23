from collections import Counter
for _ in range(int(input())):
    n=int(input())
    s=input()
    w=set()
    count= Counter(s)
    l=0
    r=len(set(s))
    c=r

    for ch in s:
        if ch not in w:
            l+=1
        if count[ch]==1:
            r-=1

        count[ch]-=1
        c=max(l+r, c)
        w.add(ch)

    print(c)