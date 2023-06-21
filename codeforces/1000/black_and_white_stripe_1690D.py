for _ in range(int(input())):
    n, k = list(map(int,input().split()))
    s = input().strip()

    f = s[:k].count("B")
    m=f

    for i in range(k, n):
        if s[i]=='B':
            f+=1
        if s[i-k]=='B':
            f-=1
        m=max(m, f)

    print(0 if m>=k else k-m)