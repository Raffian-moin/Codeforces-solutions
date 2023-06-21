for _ in range(int(input())):
    n=int(input())
    s=input()
    z=set(s[0])

    for i in range(1, n):
        if s[i]!=s[i-1] and s[i] in z:
            print('NO')
            break
        z.add(s[i])
    else:
        print('YES')