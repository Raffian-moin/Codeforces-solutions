n = int(input())

while n:
    competitors  = int(input())
    strengths = list(map(int,input().split()))

    sort_strength = sorted(strengths)

    max_strength = sort_strength[len(sort_strength)-1]

    for index in range(len(strengths)):
        diff = strengths[index] - max_strength
        if strengths[index] == max_strength:
            diff = max_strength - sort_strength[len(sort_strength)-2]
        print(diff)
    
    n = n -1