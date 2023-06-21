for _ in range(int(input())):
    n, r, b = list(map(int,input().split()))

    count = r//(b+1)
    remainder = r%(b+1)
    string = ''

    for _ in range(b+1):
        if remainder!= 0:
            string+= 'R'*(count+1)
            remainder-= 1
        else:
            string+= 'R'*(count)
        if b!= 0:
            string+= 'B'
            b-=1

    print(string)
