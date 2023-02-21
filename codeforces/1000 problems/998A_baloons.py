n = int(input())
arr = list(map(int,input().split()))

if n<3 and len(set(arr))==1:
    print('-1')
else:
    print('1')
    print(arr.index(min(arr))+1)