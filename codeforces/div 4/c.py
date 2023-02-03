for _ in range(int(input())):
    n = int(input())
    string = input()
    count = 0
    first = 0
    last = n-1

    for i in range(n//2):
        if string[first] != string[last]:
            count = count+1
            first = first+1
            last = last-1
        else:
            break



    print(n-(count*2))