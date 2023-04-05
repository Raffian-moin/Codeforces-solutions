for _ in range(int(input())):
    n, k=list(map(int, input().split()))
    s=input()

    for i in range(n):
        if k>int(s[i]):
            print(s[:i]+str(k)+s[i:])
            break
    else:
        print(s+str(k))