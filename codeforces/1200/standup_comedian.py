for _ in range(int(input())):
    a1, a2, a3, a4=list(map(int, input().split()))
 
    if a1==0:
        print(1)
    else:
        print(a1+min(a2, a3)*2+min(a1+1, abs(a2-a3)+a4))