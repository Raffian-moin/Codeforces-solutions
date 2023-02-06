n = int(input())
flats = list(map(int, input().split()))
count = 0
for i in range(1, n-2):
    if flats[i] == 0 and flats[i-1] == 1 and flats[i+1] == 1:
        count = count+1

print(count)