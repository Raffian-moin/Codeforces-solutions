for _ in range(int(input())):
    n = int(input())
    final = list(map(int, input().split()))

    for i in range(n):
        d, move = list(input().split())
        
        for j in range(len(move)-1, -1, -1):
            if move[j] == 'D':
                final[i] = (final[i]+1+10)%10
            else: 
                final[i] = (final[i]+10-1)%10

    print(*final)