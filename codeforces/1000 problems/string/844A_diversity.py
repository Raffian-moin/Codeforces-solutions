s = input()
k = int(input())

if k > len(s):
    print('impossible')
else:
    print(max(0, k-len(set(s))))