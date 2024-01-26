from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    s = input()
    charCount = defaultdict(int)
    charMax = 0

    for ch in s:
        charCount[ch] += 1
        charMax = max(charMax, charCount[ch])

    print(charMax - (n- charMax) if charMax > n//2 else n%2)

