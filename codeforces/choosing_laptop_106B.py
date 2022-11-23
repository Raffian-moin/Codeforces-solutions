tets_cases = int(input())
arr = []
while tets_cases:
    arr.append(list(map(int, input().split())))
    
    tets_cases = tets_cases-1

print(arr)