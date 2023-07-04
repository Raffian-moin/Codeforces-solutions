import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=sorted(list(map(int, input().split())), reverse=True)
    s=set()

    for el in a:
        while(el>n or el in s):
            el=el//2

        if el==0:
            print('NO')
            break
        else:
            s.add(el)
    else:
        print('YES')