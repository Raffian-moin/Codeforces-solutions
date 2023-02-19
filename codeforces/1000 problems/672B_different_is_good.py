n = int(input())
s = len(set(input()))

print('-1' if n>26 else n-s)
