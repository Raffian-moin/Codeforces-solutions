for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]

    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            b.append(a[i])

    count = 1
    for i in range(1, len(b) - 1):
        if (b[i] > b[i - 1] and b[i] > b[i + 1]) or (b[i] < b[i - 1] and b[i] < b[i + 1]):
            count += 1

    if (len(b) > 1):
        count += 1
        
    print(count)