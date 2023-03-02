for _ in range(int(input())):
    n = int(input())
    s = input().lower()
    t = s[0]

    for i in range(1, n):
        if s[i] != t[len(t)-1]:
            t+= s[i]

    print('YES' if t=='meow' else 'NO')
