for _ in range(int(input())):
    n = int(input())
    s = input()
    d = ''
    for i in range(1, 100):
        if i%3 == 0:
            d+='F'
        if i%5 ==0:
            d+='B'

    if s in d:
        print('YES')
    else:
        print('NO')
