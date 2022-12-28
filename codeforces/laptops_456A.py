n = int(input())

price = 0
quality = 0
ans = 'Poor Alex'

for i in range(n):
    a, b = input().split()
    if i==0:
        price = a
        quality = b
    if a > price and b < quality:
        ans = 'Happy Alex'
    else:
        price = a
        quality = b

print(ans)