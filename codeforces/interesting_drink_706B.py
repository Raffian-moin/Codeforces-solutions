import bisect  
n=int(input())
l = list(map(int, input().split()))
d = int(input())
l.sort()

for i in range(d):
    coins = int(input())
    print(bisect.bisect(l, coins))  
