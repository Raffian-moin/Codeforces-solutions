for _ in range(int(input())):
    n=int(input())
    s=input()
    d=set()

    for i in range(n-1):
        d.add(s[i]+s[i+1])

    print(len(d))