from collections import defaultdict
for _ in range(int(input())):
    n,d=list(map(int, input().split()))
    a=list(map(int, input().split()))

    myDict=defaultdict(int)


    for i in range(1, 11):
        last_digit=(d*i)%10
        if last_digit not in myDict:
            myDict[last_digit]=i

    for el in a:
        last_digit=el%10
        if (last_digit in myDict and myDict[last_digit] <= el//d) or d*10 <=el:
            print('YES')
        else:
            print('NO')