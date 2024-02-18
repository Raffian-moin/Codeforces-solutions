from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dic = defaultdict(int)

    for i in range(n):

        dic[a[i]] = b[i]

    for j in range(n):
        a[j] = j + 1
        b[j] = dic[a[j]]


    print(*a)
    print(*b)