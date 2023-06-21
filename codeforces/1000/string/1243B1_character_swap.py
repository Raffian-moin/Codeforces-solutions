for _ in range(int(input())):
    n = int(input())

    s = input()
    t = input()
    arr = []
    for i in range(n):
        if s[i] != t[i]:
            arr.append([s[i], t[i]])

    if len(arr) == 2 and arr[0] == arr[1]:
        print('Yes')
    else:
        print('No')

# didn't notice the word "distinct" strings
# and also character should be swapped between strings not within themselves