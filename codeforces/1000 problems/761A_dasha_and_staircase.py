a, b = list(map(int, input().split()))

print('NO' if abs(a-b) > 1 or max(a, b) < 1  else 'YES')
    