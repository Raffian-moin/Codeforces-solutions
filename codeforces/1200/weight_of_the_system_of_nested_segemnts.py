for _ in range(int(input())):
    input()
    n,m=map(int, input().split())
    d=[[i+1]+list(map(int,input().split())) for i in range(m)]

    d=sorted(d,key=lambda p: p[2])[:n*2]
    d=sorted(d, key=lambda q: q[1])

    print(sum([i[2] for i in d]))

    z=0
    while z<n:
        print(d[z][0], d[n*2-z-1][0])
        z+=1

