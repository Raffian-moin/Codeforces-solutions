n = int(input())
s = input()

if len(set(s)) == 1:
    print('NO')
else:
    for i in range(n-1):
        if s[i] != s[i+1]:
            print('YES')
            print(s[i:i+2])
            break

# same logic but with less if else
# for i in range(n-1):
#         if s[i] != s[i+1]:
#             print('YES')
#             print(s[i:i+2])
#             break
# else:
#     print('NO')


