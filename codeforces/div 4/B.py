for _ in range(int(input())):
    cor = [0, 0]
    n = int(input())
    string = input()

    for i in range(n):
        if string[i] == 'U':
            cor[1] = cor[1]+1
        elif string[i] == 'D':
            cor[1] = cor[1]-1
        elif string[i] == 'R':
            cor[0] = cor[0]+1
        else:
            cor[0] = cor[0]-1
        
        if cor[0] == 1 and cor[1] == 1:
            print('YES')
            break
    else:
        print('NO')