import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    a=[a[-1]]+a
    b=[b[-1]]+b

    for i in range(n, 0, -1):
        if (b[i-1]!=a[i-1] and b[i-1]-b[i]>1) or a[i]>b[i]:
            print('NO')
            break
    else:
        print('YES')

    # another approach without array merging

    # for i in range(n)
    # a[i] > b[i] and b[i] - b[(i + 1) % n] > 1 and b[i-1]!=a[i-1]