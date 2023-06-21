for _ in range(int(input())):
    s = input()
    t = input()

    if 'a' in t and len(t)>1:
        print(-1)
    elif 'a' in t and len(t)==1:
        print(1)
    else:
        print(2**len(s))

# ===can also be written as=== 

# if t == "a":
#         print(1)
#     elif t.count('a') != 0:
#         print(-1)
#     else:
#         print(2**len(s))