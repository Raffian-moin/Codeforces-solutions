for _ in range(int(input())):
    n=int(input())

    a=list(map(str, input().split()))
    a.sort(key=len)

    if "".join(reversed(a[-1])) == a[-2]:
        print('YES')
    else:
        print('NO')