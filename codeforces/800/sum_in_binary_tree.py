for _ in range(int(input())):
    n = int(input())
    x = 1<< n.bit_length()-1
    c = n-x
    m = n

    while(x>=1):
        x=x//2
        c=c//2
        m+=x+c
        
    print(m)