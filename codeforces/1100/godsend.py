n=int(input())
a=list(map(int, input().split()))

for el in a:
    if el&1:
        print('First')
        break
else:
    print('Second')