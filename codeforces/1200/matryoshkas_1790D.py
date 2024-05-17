from collections import Counter

for _ in range(int(input())):
    n = int(input())

    a = sorted(list(map(int, input().split())))

    x = Counter(a)

    prev = 0
    prev_freq = 0
    ans = 0

    for el in x:
        if (prev + 1 == el):
            if x[el] > prev_freq:
                ans += x[el] - prev_freq
        else:
            ans += x[el]

        prev = el
        prev_freq = x[el]

    print(ans)
