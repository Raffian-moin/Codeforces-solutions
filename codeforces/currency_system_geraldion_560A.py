n = int(input())
input = list(map(int, input().split()))

input.sort()

if input[0] > 1:
    print(1)
else:
    print(-1)