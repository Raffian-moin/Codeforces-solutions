for _ in range(int(input())):
    s=input()
    l=len(set(s))
    
    if len(set(s[:l]))!=l:
        print('NO')
    else:
        for i in range(l, len(s)):
            if s[i]!=s[i-l]:
                print('NO')
                break
        else:
            print('YES')

    # we don't need outer if condition
    # let's think why