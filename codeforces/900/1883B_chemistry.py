from collections import Counter
for _ in range(int(input())):
    n, k = map(int, input().split())

    test_str = input()

    count = Counter(test_str)

    ones = 0
    odds = 0
    
    for letter, frequency in count.items():
        if frequency == 1:
            ones += 1
        elif frequency&1:
            odds +=1

    removed_letters = 0

    if ones > 0:
        removed_letters = ones - 1 + odds
    elif odds > 0:
        removed_letters = odds - 1

    if k < removed_letters:
        print('NO')
    else:
        print("YES")

# Elegant solution
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     l = input()
#     s = 0
#     for i in set(l):
#         s += (l.count(i) % 2)
#     if s <= b + 1:
#         print("YES")
#     else:
#         print("NO")
 