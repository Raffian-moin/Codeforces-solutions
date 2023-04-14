for _ in range(int(input())):
    n=int(input())
    s = input()

    for i in range(n-1):
        if s.count(s[i:i+2]) > 1:
            print('YES')
            break
    else:
        print('NO')