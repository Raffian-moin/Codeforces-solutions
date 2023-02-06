t = int(input())

while t:
    n = int(input())
    sum = 1
    for i in range(2, n+1):
        sum = sum + ((i*2)-1)*i
    sum*=2022
    print(sum % (10**9 + 7))
    t = t-1
