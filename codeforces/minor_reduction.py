t = int(input())

while t:
    n = input()
    if int(n[len(n)-1])+int(n[len(n)-2]) <10:
        sum = (str(int(n[0])+int(n[1])))+n[2:]
    else:
        sum = n[0:(len(n)-2)]+str(int(n[len(n)-1])+int(n[len(n)-2]))
    print(int(sum))

    t=t-1