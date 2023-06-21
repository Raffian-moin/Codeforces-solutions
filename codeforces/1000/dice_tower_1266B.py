n = int(input())
favorite_numbers = list(map(int, input().split()))

for number in favorite_numbers:
    print('YES' if number>14 and 1 <= number%14 <= 6 else 'NO')